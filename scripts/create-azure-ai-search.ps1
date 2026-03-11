#Requires -Version 5.1
<#
.SYNOPSIS
    Deploys an Azure AI Search instance (Free tier), creates an index, and
    uploads the News Story markdown files from the data/ directory.

.DESCRIPTION
    PowerShell equivalent of create-azure-ai-search.sh for running on Windows.
#>

$ErrorActionPreference = 'Stop'

# -- Variables ----------------------------------------------------------------
$ResourceGroup    = 'agenticodyssey-rg'
$Location         = 'westus3'
$SearchServiceName = if ($env:SEARCH_SERVICE_NAME) { $env:SEARCH_SERVICE_NAME } else { "agenticodyssey-search-$(Get-Random -Maximum 32767)" }
$IndexName        = if ($env:INDEX_NAME) { $env:INDEX_NAME } else { 'news-stories' }
$ApiVersion       = '2024-07-01'

$RepoDir = Split-Path -Parent $PSScriptRoot
$DataDir = Join-Path $RepoDir 'data'

# -- Prerequisite Checks -----------------------------------------------------
Write-Host '=== Checking prerequisites ==='

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    Write-Error 'Azure CLI (az) is not installed. Install it from https://aka.ms/installazurecliwindows'
}

$null = az account show 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "Not logged in to Azure. Run 'az login' first."
}

Write-Host 'All prerequisites met.'

# -- Create Resource Group ----------------------------------------------------
Write-Host ''
Write-Host "=== Creating resource group: $ResourceGroup ==="
az group create --name $ResourceGroup --location $Location --output none
if ($LASTEXITCODE -ne 0) { Write-Error 'Failed to create resource group.' }
Write-Host "Resource group '$ResourceGroup' ready."

# -- Create Azure AI Search Service (Free tier) -------------------------------
Write-Host ''
Write-Host "=== Creating Azure AI Search service: $SearchServiceName (Free tier) ==="
az search service create `
    --name $SearchServiceName `
    --resource-group $ResourceGroup `
    --sku free `
    --location $Location `
    --output none
if ($LASTEXITCODE -ne 0) { Write-Error 'Failed to create search service.' }
Write-Host "Search service '$SearchServiceName' created."

# -- Retrieve Admin API Key ---------------------------------------------------
Write-Host ''
Write-Host '=== Retrieving admin API key ==='
$AdminKey = az search admin-key show `
    --service-name $SearchServiceName `
    --resource-group $ResourceGroup `
    --query primaryKey `
    --output tsv
if ($LASTEXITCODE -ne 0) { Write-Error 'Failed to retrieve admin key.' }

$SearchEndpoint = "https://${SearchServiceName}.search.windows.net"
Write-Host 'Admin key retrieved.'

# -- Create Search Index ------------------------------------------------------
Write-Host ''
Write-Host "=== Creating search index: $IndexName ==="

$IndexSchema = @{
    name   = $IndexName
    fields = @(
        @{ name = 'id';      type = 'Edm.String'; key = $true;  searchable = $false; filterable = $false; sortable = $false; facetable = $false }
        @{ name = 'title';   type = 'Edm.String'; key = $false; searchable = $true;  filterable = $false; sortable = $false; facetable = $false }
        @{ name = 'date';    type = 'Edm.String'; key = $false; searchable = $false; filterable = $true;  sortable = $true;  facetable = $false }
        @{ name = 'type';    type = 'Edm.String'; key = $false; searchable = $true;  filterable = $true;  sortable = $false; facetable = $true  }
        @{ name = 'region';  type = 'Edm.String'; key = $false; searchable = $true;  filterable = $true;  sortable = $false; facetable = $true  }
        @{ name = 'content'; type = 'Edm.String'; key = $false; searchable = $true;  filterable = $false; sortable = $false; facetable = $false }
    )
} | ConvertTo-Json -Depth 5

$Headers = @{
    'Content-Type' = 'application/json'
    'api-key'      = $AdminKey
}

$null = Invoke-RestMethod `
    -Uri "${SearchEndpoint}/indexes/${IndexName}?api-version=${ApiVersion}" `
    -Method Put `
    -Headers $Headers `
    -Body $IndexSchema

Write-Host "Index '$IndexName' created."

# -- Upload News Story Documents ----------------------------------------------
Write-Host ''
Write-Host '=== Uploading News Story documents ==='

$Documents = @()

foreach ($file in Get-ChildItem -Path $DataDir -Filter 'News Story*.md') {
    Write-Host "  Processing: $($file.Name)"

    # Generate a stable ID from the filename
    $docId = $file.BaseName -replace '[^a-zA-Z0-9]', '-'
    $docId = $docId.ToLower() -replace '-+', '-' -replace '^-|-$', ''

    $fileContent = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Extract metadata
    $title     = ($fileContent -split "`n" | Where-Object { $_ -match '^# ' }    | Select-Object -First 1) -replace '^# ', ''
    $dateVal   = ($fileContent -split "`n" | Where-Object { $_ -match '^\*\*Date:\*\*' }   | Select-Object -First 1) -replace '.*\*\*Date:\*\*\s*', ''
    $typeVal   = ($fileContent -split "`n" | Where-Object { $_ -match '^\*\*Type:\*\*' }   | Select-Object -First 1) -replace '.*\*\*Type:\*\*\s*', ''
    $regionVal = ($fileContent -split "`n" | Where-Object { $_ -match '^\*\*Region:\*\*' } | Select-Object -First 1) -replace '.*\*\*Region:\*\*\s*', ''

    $Documents += @{
        '@search.action' = 'upload'
        id               = $docId
        title            = $title.Trim()
        date             = $dateVal.Trim()
        type             = $typeVal.Trim()
        region           = $regionVal.Trim()
        content          = $fileContent
    }
}

$BatchPayload = @{ value = $Documents } | ConvertTo-Json -Depth 5 -Compress

$UploadResponse = Invoke-RestMethod `
    -Uri "${SearchEndpoint}/indexes/${IndexName}/docs/index?api-version=${ApiVersion}" `
    -Method Post `
    -Headers $Headers `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($BatchPayload)) `
    -ContentType 'application/json; charset=utf-8'

Write-Host 'Documents uploaded successfully.'

# -- Verify Document Count ----------------------------------------------------
Write-Host ''
Write-Host '=== Verifying index ==='

Start-Sleep -Seconds 3

$DocCount = Invoke-RestMethod `
    -Uri "${SearchEndpoint}/indexes/${IndexName}/docs/`$count?api-version=${ApiVersion}" `
    -Method Get `
    -Headers $Headers

Write-Host "Documents in index '${IndexName}': $DocCount"

# -- Print Connection Info ----------------------------------------------------
Write-Host ''
Write-Host '==========================================='
Write-Host '  Azure AI Search Deployment Complete'
Write-Host '==========================================='
Write-Host "  Resource Group : $ResourceGroup"
Write-Host "  Search Service : $SearchServiceName"
Write-Host "  Endpoint       : $SearchEndpoint"
Write-Host "  Index Name     : $IndexName"
Write-Host "  Admin Key      : $AdminKey"
Write-Host "  Documents      : $DocCount"
Write-Host '==========================================='
Write-Host ''
Write-Host 'Test with:'
Write-Host "  Invoke-RestMethod -Uri '${SearchEndpoint}/indexes/${IndexName}/docs?api-version=${ApiVersion}&search=chicken&`$top=3' -Headers @{'api-key'='${AdminKey}'}"
