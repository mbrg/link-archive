---
date: '2025-08-13'
description: The latest installment in the "Detection as Code" series discusses implementing
  validation checks for detection repositories, enhancing reliability and quality.
  It emphasizes using Azure DevOps pipelines for schema validation, query syntax checks,
  and structural integrity of detection files. Key strategies include JSON schema
  enforcement, query syntax validation via Kusto.Language.dll, and reference checking.
  The article also outlines automated workflows for these validations, ensuring adherence
  to standards while minimizing manual errors. This approach promotes consistency
  and mitigates risks in detection codebases, crucial for effective cybersecurity
  practices.
link: https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/
tags:
- Detection-as-Code
- Azure DevOps
- JSON Schema
- Validation
- Detection Engineering
title: 'Detection Engineering: Practicing Detection-as-Code - Validation - Part 3'
---

[Skip to content](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/#content)

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)August 5, 2025August 12, 202539 Minutes

This entry is part 3 in the series [Detection Engineering: Practicing Detection-as-Code](https://blog.nviso.eu/series/detection-engineering-practicing-detection-as-code/ "Detection Engineering: Practicing Detection-as-Code")

* * *

In [Part 2](https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/) of the series, we covered the basics of designing a repository to store detections and established the format and structure for detections and content packs.

In this part, we focus on implementing validation checks to improve consistency and ensure a minimum level of quality within the detection repository. Setting up validation pipelines is a key step, as it helps enforce the defined standards, reduce errors, and ensure that detections are reliable and consistent. We’ll break the validation process into several smaller scripts and pipelines that you can refer to when building your own validation workflows. This approach also helps make the content of this blog post easier to digest.

## Repository Branch Policies

In [Part 1](https://blog.nviso.eu/2025/07/08/detection-engineering-practicing-detection-as-code-introduction-part-1/) of this blog series, we included a diagram illustrating how adopting Detection-as-Code requires that changes to detection code undergo manual peer review. In Azure DevOps Repos, this principle can be implemented and enforced using repository branch policies. Branch policies help ensure that our quality controls are followed, such as requiring pull requests for changes, mandating code reviews by team members, setting a minimum number of reviewers, running validation pipelines, and verifying that all comments are resolved before changes are merged.

We can configure branch policies for our repository in Azure DevOps under the repository settings and the policies tab of the main branch.

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-11.png)![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-12.png)

## Validation Checks

Regarding the types of validation checks we can implement, we have included the following:

- **Detections**
  - **Schema** – Check that structured files in detections (e.g., JSON, YAML) conform to their defined schemas.
  - **Query syntax** – Validate that detection queries use correct syntax for the target platform.
  - **References** – Ensure that all referenced URLs in metadata files are not broken.
  - **Spelling** – Scan metadata files for spelling errors to maintain quality and clarity.
- **Content Packs**
  - **Schema** – Check that content packs conform to their defined schemas.
  - **References** – Verify that all detections referenced by content packs actually exist within the repository.
- **Repository**
  - **Structure** – Ensure that required directories (e.g. detections/, parsers/, content\_packs/ etc.) are present, naming conventions (e.g. lowercase, proper prefixes/suffixes) are followed, and that each directory contains the expected files.

Before moving forward with automating these validation checks, we’ll first talk a bit about Azure Pipelines \[1\] and JSON schemas \[2\].

## Azure Pipelines

Azure Pipelines is a component of Azure DevOps that automatically builds, tests, and deploys code projects. We will be using Azure Pipelines in this blog series, however there are other alternatives, like GitHub Actions or AWS CodePipeline, depending on the Git platform you selected.

In Azure DevOps, a pipeline may consist of the following basic components \[3\]:

- **Triggers** that define when the pipeline should start, typically based on code changes in specific branches or parts of the code.
- **Stages** that organize the pipeline into major phases, such as build, test, and deploy, each containing multiple jobs.
- **Jobs** that are units of work executed on agents, potentially running tasks in parallel.
- **Steps** that are defined within jobs and are the individual tasks or scripts that perform specific actions, like installing dependencies or executing scripts.

As an example, the following pipeline will execute the script example.py whenever changes on the main branch occur that include a JSON file.

```

```

```
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - "*.json"

stages:
- stage: ExampleStage
  displayName: "Example Stage"
  jobs:
  - job: ExampleJob
    displayName: "Example Job"
    steps:
    - script: |
        python scripts/example.py
      displayName: 'Execute Example Script'
```

YAML

## JSON Schemas

A JSON schema defines the rules and structure that JSON data must follow. It specifies elements such as required fields, accepted data types (e.g., string, number, boolean), and allowed values. This helps identify human errors early, such as missing fields, incorrect data types, invalid values, or typos. By defining validation schemas for the repository’s detections and content packs, we can ensure consistency across the codebase and improve the overall reliability and quality of the detection library.

An example JSON structure and its corresponding schema are shown below. The schema includes a string field that allows only letters and spaces, with a minimum length of 5 and a maximum of 20 characters. A number field is constrained to values between 0 and 100. A boolean field accepts true or false values, while a null field explicitly allows null values. Additionally, there is an array field that must contain between 2 and 5 unique strings, each string having at least 3 characters. The schema also enforces required properties and forbids any additional unspecified fields.

```

```

```
{
  "string_example": "string example",
  "integer_example": 42,
  "boolean_example": true,
  "null_example": null,
  "array_example": ["item1", "item2", "item3"]
}
```

JSON

```

```

```
{
  "title": "ExampleDataTypes",
  "type": "object",
  "properties": {
    "string_example": {
      "type": "string",
      "minLength": 5,
      "maxLength": 20,
      "pattern": "^[a-zA-Z\\s]+$",
      "description": "A string with length between 5 and 20, letters and spaces only"
    },
    "integer_example": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "An integer between 0 and 100"
    },
    "boolean_example": {
      "type": "boolean",
      "description": "A boolean value, true or false"
    },
    "null_example": {
      "type": "null",
      "description": "A null value"
    },
    "array_example": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 3
      },
      "minItems": 2,
      "uniqueItems": true,
      "description": "An array of unique strings, each at least 3 characters, with at least 2 items"
    }
  },
  "required": ["string_example", "integer_example", "boolean_example", "array_example"],
  "additionalProperties": false
}

```

JSON

We can easily validate JSON structures against a schema with just a few lines of Python code. We will be using the following script to validate metadata files, rule files, and content packs. The script first loads the schema, then recursively searches a specified directory for files matching a given regex pattern. For each matched file, it parses the content – using yaml.safe\_load for YAML files (safe\_load will convert the yaml structure to a dictionary object) and json.load for JSON files. It then runs validation against the schema and logs any validation errors or exceptions encountered during parsing or validation.

```

```

```
import os
import sys
import yaml
import json
import logging
import argparse
import re
from jsonschema import Draft7Validator, SchemaError

def validate(schema_path: str, files_dir: str, file_regex: str):
    # Load and validate the schema
    try:
        with open(schema_path, "r") as f:
            schema = json.load(f)
        validator = Draft7Validator(schema)
    except SchemaError as se:
        logging.error(f"##vso[task.logissue type=error]Invalid schema: {se}")
        sys.exit(1)
    except json.JSONDecodeError as jde:
        logging.error(f"##vso[task.logissue type=error]Failed to parse schema JSON: {jde}")
        sys.exit(1)

    # Collect matching files
    matched_files = []
    pattern = re.compile(file_regex)
    for root, _, files in os.walk(files_dir):
        for file in files:
            full_path = os.path.join(root, file)
            if pattern.search(file):
                matched_files.append(full_path)

    if not matched_files:
        logging.error("##vso[task.logissue type=error]No files found to validate matching regex.")
        sys.exit(1)

    # Validate each matched file
    has_errors = False
    for file_path in matched_files:
        try:
            with open(file_path, "r") as f:
                if file_path.endswith((".yml", ".yaml")):
                    data = yaml.safe_load(f)
                else:
                    data = json.load(f)

            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if errors:
                has_errors = True
                for error in errors:
                    location = ".".join([str(p) for p in error.path])
                    if location == "":
                        location = '<root>'
                    logging.error(
                        f"##vso[task.logissue type=error]{file_path} → {location}: {error.message}"
                    )
        except Exception as e:
            has_errors = True
            logging.error(f"##vso[task.logissue type=error]{file_path} → {str(e)}")

    # Exit with 1 if any file failed
    if has_errors:
        logging.error("Errors while validating files!")
        sys.exit(1)

    logging.info(f"All files validated successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate YAML/JSON files against a JSON schema.")
    parser.add_argument("--schema", required=True, help="Path to the JSON schema file.")
    parser.add_argument(
        "--file-dir",
        required=True,
        help="Path to the directory containing files to validate.",
    )
    parser.add_argument(
        "--file-regex-filter",
        required=False,
        help="Regex to filter filenames (e.g., '_meta.yaml|_sentinel.json').",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    validate(args.schema, args.file_dir, args.file_regex_filter)

```

Python

## Detections Validation

With the pipeline and JSON schema basics established, the next step is to define schemas for both metadata files and detection rules we will store in the repository.

### Metadata Files Validation

The JSON schema ensures that the metadata file, defined in [Part 2](https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/), contains all the required fields, populated with correct types and adhering to constraints. It validates that strings like name and description meet minimum length requirements, level matches specific values (low, medium, high), and arrays such as references, investigation\_steps, and tags are not empty and contain unique items. Also, for tags, we make sure that they follow a strict naming pattern.

```

```

```
{
  "type": "object",
  "required": ["title", "id", "description", "version", "level", "references", "data_source", "blindspots", "known_false_positives", "investigation_steps", "tags"],
  "properties": {
    "name": {
      "type": "string",
      "minLength": 10
    },
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$"
    },
    "description": {
      "type": "string",
      "minLength": 50
    },
    "level": {
      "type": "string",
      "enum": ["low", "medium", "high"]
    },
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$"
    },
    "references": {
      "type": "array",
      "items": {
        "type": "string"
      },
	  "minItems": 1,
      "uniqueItems": true
    },
    "data_source": {
      "type": "object",
      "required": ["category", "vendor", "product", "event_source", "event_ids"],
      "properties": {
        "category": {
          "type": "string"
        },
        "vendor": {
          "type": "string"
        },
        "product": {
          "type": "string"
        },
        "event_source": {
          "type": "string"
        },
        "event_ids": {
          "type": ["string", "integer", "null"]
        }
      }
    },
    "blindspots": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "known_false_positives": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "investigation_steps": {
      "type": "array",
      "items": {
        "type": "string"
      },
	  "minItems": 1,
      "uniqueItems": true
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^(tactic\\.(?:reconnaissance|resource_development|initial_access|execution|persistence|privilege_escalation|defense_evasion|credential_access|discovery|lateral_movement|collection|command_and_control|exfiltration|impact|evasion)|technique\\.t\\d{4}(?:\\.\\d{3})?|group\\.g\\d{4}|software\\.s\\d{4}|car\\.\\d{4}\\-\\d{2}\\-\\d{3}|cve\\.\\d{4}\\-\\d{,6}|notable\\.[a-z0-9_]+)$"
       },
	 "minItems": 1,
     "uniqueItems": true
    }
  }
}
```

JSON

The next step is to create a pipeline in our Azure DevOps project that triggers on every branch whenever a file with the suffix \_meta.yml under the detections directory is modified. Once triggered, the pipeline will run a job that executes the validate\_schema.py script.

```

```

```
name: Validate Detection Metadata

trigger:
  branches:
    include:
      - '*'
  paths:
    include:
      - '*_meta.yml'

jobs:
- job: ValidateDetectionMetadata
  displayName: "Validate Detection Metadata"
  steps:
    - checkout: self
    - script: |
        python pipelines/scripts/validate_schema.py --schema pipelines/schemas/detection_meta_schema.json --file-dir detections --file-regex-filter "_meta\.yml"
      displayName: 'Run Detection Metadata Validation'

```

YAML

After saving the pipeline, we also need to configure build validation \[4\] for our main branch. The build validation policy ensures that a pull request cannot be completed if the build has failed by selecting the Required option under Policy Requirement. This means that if errors are identified while validating metadata files against their schema, we will not be allowed to merge the branch we are working on into the main branch.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-27.png)

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-19-1024x145.png)

Upon creating a pull request to our main branch, the build validation runs and identifies any potential issues with the committed detections. For example, the validation of the schema below identified a short description, an empty known\_false\_positives array, and an incorrect value for the level field.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-64.png)

### Rule Files Validation

For rule files, you need to define a schema according to the platforms you support. As an example, we provide a rule validation schema for Sentinel analytics rules. This schema validates the overall structure, ensuring that all required fields are present. It also enforces minimum lengths for the displayName and description fields, restricts severity to one of “Low,” “Medium,” or “High,” and ensures that each rule is enabled. Arrays such as tactics and techniques must contain at least one item. Additionally, the schema verifies that all stored rules are configured to create incidents.

Defining that schema is important as it helps us prevent scenarios where a disabled rule or a rule that does not generate incidents is accidentally stored in the repository and deployed to production under the false assumption that it is active.

```

```

```
{
  "type": "object",
  "required": ["id", "name", "type", "kind", "apiVersion", "properties"],
  "properties": {
    "properties": {
      "type": "object",
      "required": ["displayName", "description", "severity", "enabled", "query","queryFrequency", "queryPeriod", "triggerOperator", "triggerThreshold","suppressionDuration", "suppressionEnabled", "tactics", "techniques", "incidentConfiguration"],
      "properties": {
        "displayName": {
          "type": "string",
          "minLength": 10
        },
        "description": {
          "type": "string",
          "minLength": 50
        },
        "severity": {
          "type": "string",
          "enum": ["Low", "Medium", "High"]
        },
        "enabled": {
          "type": "boolean",
          "const": true
        },
        "query": {
          "type": "string",
          "minLength": 5
        },
        "tactics": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string"
          }
        },
        "techniques": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string"
          }
        },
        "incidentConfiguration": {
          "type": "object",
          "required": ["createIncident"],
          "properties": {
            "createIncident": {
              "type": "boolean",
              "const": true
            }
          }
        }
      }
    }
  }
}

```

JSON

Similar to the metadata file we will configure a pipeline to run the script and perform the validation.

```

```

```
name: Validate Sentinel Detections

trigger:
  branches:
    include:
      - '*'
  paths:
    include:
      - '*_sentinel.json'

jobs:
- job: ValidateSentinelDetections
  displayName: "Validate Sentinel Detections"
  steps:
    - checkout: self
    - script: |
        python pipelines/scripts/validate_schema.py --schema pipelines/schemas/detection_sentinel_schema.json --file-dir detections --file-regex-filter "_sentinel\.json"
      displayName: 'Run Sentinel Detection Validation'
```

YAML

We add the pipeline to the build validation of our main branch so that it runs and identifies potential issues with the committed detections when we create pull requests.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-20-1024x190.png)

An example output of the Sentinel schema build validation, where a disabled rule was committed to the repository, is shown below.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-69.png)

### Query Syntax Validation

With query syntax validation in our validation pipelines, we can ensure reliability in the detection rules. Depending on the platform(s) you support you may not find available syntax validation libraries that you can use and may need to write your own from scratch. There are a bunch of related projects and reference material \[5\]\[6\]\[7\]\[8\]\[9\] that you can check and may be able to adapt to your workflows.

As an example, we’re going to create a KQL syntax validator pipeline for Sentinel rules. We’ll use the Microsoft.Azure.Kusto.Language package from NuGet, which is a .NET language service for the Kusto Query Language. We’ll also use Pythonnet, a Python package that allows us to interact with .NET code directly from Python. The script below extracts Sentinel table and function definitions (a.k.a. manifests) embedded in Microsoft.Azure.Sentinel.KustoServices.dll and validates the provided KQL queries using the ParseAndAnalyze function of the Kusto.Language.dll.

```

```

```
import pythonnet

pythonnet.set_runtime("coreclr")
import clr
import os
import re
import json
import argparse
import sys
import logging
from collections import UserDict
from System import Reflection
from System.IO import StreamReader
from System.Collections.Generic import List

clr.AddReference("System.Collections")

class CaseInsensitiveDict(UserDict):
    """Custom dictionary class that handles case-insensitive keys"""
    def __init__(self, data=None, **kwargs):
        super().__init__()
        if data:
            self.update(data)
        if kwargs:
            self.update(kwargs)

    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, self.to_case_insensitive(value))

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

    def __delitem__(self, key):
        super().__delitem__(key.lower())

    def __contains__(self, key):
        return super().__contains__(key.lower())

    def get(self, key, default=None):
        return super().get(key.lower(), default)

    def update(self, other=None, **kwargs):
        if other:
            if hasattr(other, "keys"):
                for k in other:
                    self[k] = other[k]
            else:
                for k, v in other:
                    self[k] = v
        for k, v in kwargs.items():
            self[k] = v

    @staticmethod
    def to_case_insensitive(obj):
        """Recursively convert nested dicts/lists to case-insensitive dicts."""
        if isinstance(obj, dict) and not isinstance(obj, CaseInsensitiveDict):
            return CaseInsensitiveDict(obj)
        elif isinstance(obj, list):
            return [CaseInsensitiveDict.to_case_insensitive(item) for item in obj]
        return obj

def extract_manifests(kusto_services_dll_path: str, output_folder: str):
    """Extract embedded JSON manifest resources from the DLL"""
    logging.info(f"Extracting manifests from {kusto_services_dll_path}")

    assembly = Reflection.Assembly.LoadFile(kusto_services_dll_path)
    resource_names = assembly.GetManifestResourceNames()

    for resource_name in resource_names:
        if resource_name.endswith(".json"):
            stream = assembly.GetManifestResourceStream(resource_name)
            reader = StreamReader(stream)
            content = reader.ReadToEnd()
            reader.Close()
            stream.Close()

            parts = resource_name.split(".")
            if len(parts) < 6:
                logging.warning(f"Skipping resource: {resource_name}")
                continue

            parent_folder = parts[4]
            filename = ".".join(parts[5:])
            manifest_folder = os.path.join(output_folder, parent_folder)

            # Create directory if it doesn't exist
            if not os.path.exists(manifest_folder):
                os.makedirs(manifest_folder)

            # Write content to file
            manifest_path = os.path.join(manifest_folder, filename)
            with open(manifest_path, "w", encoding="utf-8") as f:
                f.write(content)

    # Log extracted files
    logging.info("Manifest extraction complete.")
    logging.info(f"Extracted files in {output_folder}:")
    for root, dirs, files in os.walk(output_folder):
        for file in files:
            full_path = os.path.join(root, file)
            logging.info(f"- {os.path.relpath(full_path, output_folder)}")

def normalize_type(t: str) -> str:
    return t.lower().replace("bigint", "long").replace("uri", "string").replace(" ", "")

def to_column_symbol(column, ScalarTypes):
    from Kusto.Language.Symbols import ColumnSymbol

    try:
        scalar_type = ScalarTypes.GetSymbol(normalize_type(column["Type"])) or ScalarTypes.Unknown
    except Exception as e:
        logging.error(f"Exception in column {column}: {str(e)}")
    return ColumnSymbol(column["Name"], scalar_type, column.get("description", None))

def create_table_symbol(schema: dict, ScalarTypes):
    """Create a TableSymbol from a schema definition"""
    from Kusto.Language.Symbols import TableSymbol, ColumnSymbol

    column_symbols = List[ColumnSymbol]()
    for column in schema["Properties"]:
        column_symbols.Add(to_column_symbol(column, ScalarTypes))
    return TableSymbol(schema["Name"], column_symbols, schema.get("description", None))

def create_function_symbol(schema: dict, ScalarTypes):
    """Create a FunctionSymbol from a schema definition"""
    from Kusto.Language.Symbols import (
        Parameter,
        ArgumentKind,
        FunctionSymbol,
        TableSymbol,
        ColumnSymbol,
    )

    parameter_list = List[Parameter]()
    column_symbols = List[ColumnSymbol]()

    for param in schema.get("FunctionParameters", []):
        scalar_type = ScalarTypes.GetSymbol(normalize_type(param["Type"])) or ScalarTypes.Unknown
        parameter_list.Add(
            Parameter(
                param["Name"],
                scalar_type,
                ArgumentKind.Literal,
                param.get("description", None),
            )
        )

    if not schema.get("FunctionResultColumns") and schema.get("Query"):
        return FunctionSymbol(schema["FunctionName"], schema["Query"], parameter_list, None)

    for column in schema.get("FunctionResultColumns", []):
        column_symbols.Add(to_column_symbol(column, ScalarTypes))

    return FunctionSymbol(schema["FunctionName"], TableSymbol(column_symbols), parameter_list, None)

def add_common_columns(schema: dict):
    """Add standard columns to schema definitions, like 'Type' and '_ResourceId'"""
    schema["Properties"].append({"Name": "Type", "Type": "String"})
    if schema.get("IsResourceCentric", False):
        has_resource_id = any(p["Name"] == "_ResourceId" for p in schema["Properties"])
        if not has_resource_id:
            schema["Properties"].append({"Name": "_ResourceId", "Type": "String"})

def build_global_state_from_manifests(manifests_dir: str):
    """Construct a GlobalState object from all manifest schema definitions"""
    from Kusto.Language import GlobalState
    from Kusto.Language.Symbols import ScalarTypes, Symbol, DatabaseSymbol

    symbols = List[Symbol]()

    for root, _, files in os.walk(manifests_dir):
        for file in files:
            if file.endswith(".json"):
                try:
                    logging.info(f"Global state for {file}")
                    full_path = os.path.join(root, file)
                    with open(full_path, "r", encoding="utf-8") as f:
                        schema = json.load(f)
                        schema = CaseInsensitiveDict(schema)
                    if "Properties" in schema:
                        add_common_columns(schema)
                        symbols.Add(create_table_symbol(schema, ScalarTypes))
                    elif "FunctionParameters" in schema:
                        symbols.Add(create_function_symbol(schema, ScalarTypes))
                except Exception as e:
                    logging.error(f"Exception {str(e)}")
                    logging.error(f"Schema:\n{schema}")

    db_symbol = DatabaseSymbol("default", symbols)
    return GlobalState.Default.WithDatabase(db_symbol)

def validate(kusto_dll_path: str, files_dir: str, file_regex: str, manifests_dir: str):
    """Validate KQL queries in input files using the GlobalState"""
    logging.info(f"Loading {kusto_dll_path}")
    Reflection.Assembly.LoadFile(kusto_dll_path)

    from Kusto.Language import KustoCode

    logging.info(f"Building GlobalState from manifests at {manifests_dir}")
    global_state = build_global_state_from_manifests(manifests_dir)

    # Collect all matching files
    matched_files = []
    pattern = re.compile(file_regex)
    for root, _, files in os.walk(files_dir):
        for file in files:
            full_path = os.path.join(root, file)
            if pattern.search(file):
                matched_files.append(full_path)

    if not matched_files:
        logging.error("##vso[task.logissue type=error]No files found to validate matching regex.")
        sys.exit(1)

    has_errors = False
    for file_path in matched_files:
        logging.debug(f"Processing {file_path}")
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            query = data.get("properties", {}).get("query", "")
            if not query.strip():
                logging.error(f"No query found in {file_path}")
                has_errors = True
                continue

            code = KustoCode.ParseAndAnalyze(query, global_state)
            diagnostics = code.GetDiagnostics()

            if diagnostics.Count == 0:
                logging.debug(f"[PASS] {file_path}")
            else:
                logging.warning(f"[FAIL] {file_path} — {diagnostics.Count} issue(s)")
                for msg in diagnostics:
                    # Show snippet of code around error
                    segment_start = max(msg.Start - 15, 0)
                    segment_end = min(msg.End + 15, len(query))
                    segment = "..." + query.replace("\r", "").replace("\n", "")[segment_start:segment_end] + "..."
                    logging.error(
                        f"##vso[task.logissue type=error] - {msg.Severity}: {msg.Message} [{msg.Start}-{msg.End}] -> '{segment}'"
                    )
                    if str(msg.Severity) == "Error":
                        has_errors = True

        except Exception as e:
            has_errors = True
            logging.error(f"##vso[task.logissue type=error]{file_path} → {str(e)}")

    if has_errors:
        logging.error("Errors while validating KQL queries in files!")
        sys.exit(1)

    logging.info("All files KQL queries validated successfully!")

def main():
    parser = argparse.ArgumentParser(description="Extract manifests and validate KQL using Kusto.Language.dll")
    parser.add_argument("--kusto-dll", required=True, help="Path to Kusto.Language.dll")
    parser.add_argument(
        "--services-dll",
        required=True,
        help="Path to Microsoft.Azure.Sentinel.KustoServices.dll",
    )
    parser.add_argument("--file-dir", required=True, help="Directory containing files to validate")
    parser.add_argument(
        "--file-regex-filter",
        required=True,
        default=".*",
        help="Regex to filter filenames (e.g. _sentinel.json)",
    )
    parser.add_argument(
        "--manifests-dir",
        required=False,
        default="manifests",
        help="Where to extract manifests (default: manifests)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    extract_manifests(args.services_dll, args.manifests_dir)
    validate(args.kusto_dll, args.file_dir, args.file_regex_filter, args.manifests_dir)

if __name__ == "__main__":
    main()
```

Python

The pipeline to run our KQL validation script is provided below. We first download the Microsoft.Azure.Kusto.Language package from Nuget and copy Kusto.Language.dll into the pipelines/scripts/modules directory. We also download Microsoft.Azure.Sentinel.KustoServices.dll which contains the table and function manifests (schema definitions) for Sentinel, that we are going to use to validate our queries against. We then install the required dependencies, pythonnet and the .NET runtime, and finally execute our validation script.

```

```

```
name: Validate KQL Sentinel

trigger:
  branches:
    include:
      - '*'
  paths:
    include:
      - '*_sentinel.json'

jobs:
  - job: kql_validate
    displayName: 'Validate KQL'
    pool:
      vmImage: 'ubuntu-22.04'
    steps:
      - checkout: self
      - bash: |
          mkdir -p "pipelines/scripts/modules"
          mkdir -p "pipelines/scripts/manifests"

          echo "Downloading Microsoft.Azure.Kusto.Language..."
          curl -sSL "https://www.nuget.org/api/v2/package/Microsoft.Azure.Kusto.Language/12.0.0" -o "pipelines/scripts/modules/Microsoft.Azure.Kusto.Language.12.0.0.nupkg"
          unzip -q "pipelines/scripts/modules/Microsoft.Azure.Kusto.Language.12.0.0.nupkg" -d "pipelines/scripts/modules/tmp_kusto"
          cp "pipelines/scripts/modules/tmp_kusto/lib/netcoreapp2.1/Kusto.Language.dll" "pipelines/scripts/modules"

          echo "Downloading Microsoft.Azure.Sentinel.KustoServices..."
          curl -sSL "https://github.com/Azure/Azure-Sentinel/raw/master/.script/tests/KqlvalidationsTests/Microsoft.Azure.Sentinel.KustoServices.6.7.0.nupkg" -o "pipelines/scripts/modules/Microsoft.Azure.Sentinel.KustoServices.6.7.0.nupkg"
          unzip -q "pipelines/scripts/modules/Microsoft.Azure.Sentinel.KustoServices.6.7.0.nupkg" -d "pipelines/scripts/modules/tmp_services"
          cp "pipelines/scripts/modules/tmp_services/lib/net6.0/Microsoft.Azure.Sentinel.KustoServices.dll" "pipelines/scripts/modules"

          echo "DLLs downloaded:"
          ls -lah "pipelines/scripts/modules/"
        displayName: 'Download Kusto.Language.dll and Microsoft.Azure.Sentinel.KustoServices.dll'
      - script: |
          pip install pythonnet
          pip show pythonnet

          sudo apt update
          sudo apt install -y dotnet-runtime-6.0
        displayName: Install Requirements
      - script: |
          python pipelines/scripts/validate_kql.py --kusto-dll '$(Build.SourcesDirectory)/pipelines/scripts/modules/Kusto.Language.dll' --services-dll '$(Build.SourcesDirectory)/pipelines/scripts/modules/Microsoft.Azure.Sentinel.KustoServices.dll' --manifests-dir '$(Build.SourcesDirectory)/pipelines/scripts/manifests' --file-dir 'detections/' --file-regex '.*_sentinel\.json'
        displayName: Run KQL Validation
```

YAML

We add the pipeline to the build validation and we are able to identify potential syntax errors in our KQL queries.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-28-1024x243.png)

As an example, if we were to change the frequency variable to an incorrect type like a string while the query expects it as a timespan, we would get the error below:

![](https://blog.nviso.eu/wp-content/uploads/2025/08/image-1-1024x98.png)![](https://blog.nviso.eu/wp-content/uploads/2025/08/image.png)

### URL Validation

Checking URLs is important to ensure that all links referenced in the detection library are active. To automate this process we can make use of a python module called urlchecker \[10\]. Using the module and the following pipeline, we can validate the URLs within the \_meta.yml files located in the detections/ directory.

As validating URLs is a time consuming operation and also not of critical importance in case a URL is not active, we will not include this pipeline in the Build Validation. Instead we are going to schedule it to run once per week at 02.00 so that we can review the results on a frequent basis.

```

```

```
name: Validate URLs

trigger: none

schedules:
  - cron: "0 2 * * 1"  # At 01:00 UTC every Monday
    displayName: Weekly run
    branches:
      include:
        - main

jobs:
- job: ValidateURLs
  displayName: "Validate URLs"
  steps:
    - checkout: self
    - script: |
        python -m pip install urlchecker
      displayName: Install urlchecker
    - script: |
        urlchecker check --file-types .yml --files _meta\.yml --retry-count 3 --timeout 30 detections/
      displayName: Run URL Checker
```

YAML

An example of the pipeline’s output is shown below.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-34-1024x513.png)

To be notified when the build fails we can configure the notification settings in Azure DevOps.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-98-1024x541.png)

### Spelling Validation

By validating spelling, we ensure that documentation and comments within the codebase are free from common spelling mistakes. Instead of manual review, we can automate this process using the python module codespell \[11\] and the following pipeline which will validate spelling on the detections/ directory’s yml files.

```

```

```
name: Validate Spelling

trigger:
  branches:
    include:
      - '*'
  paths:
    include:
      - '*_meta.yml'

jobs:
- job: ValidateSpelling
  displayName: "Validate Spelling"
  steps:
  - checkout: self
  - script: |
      pip install codespell
    displayName: Install codespell
  - script: |
      codespell -I pipelines/scripts/codespell_ignore.txt --skip="*.json,*.md" detections/
    displayName: Run codespell
```

YAML

We add the pipeline to the build validation and we are able to identify potential spelling errors.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-35-1024x313.png)![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-50-1024x340.png)

## Validation of Content Packs

To validate content packs we are going to check that content packs conform to their defined schema and verify that all detections referenced, exist within the repository.

The provided Python script checks for the existence of detection directories specified within each pack. If any detection directories are missing, an error message is logged, and the script exits with an error code.

```

```

```
import os
import json
import argparse
import logging

def validate_packs(content_packs_dir: str, detections_dir: str):
    errors = False

    for root, dirs, files in os.walk(content_packs_dir):
        for pack_filename in files:

            pack_path = os.path.join(content_packs_dir, pack_filename)

            try:
                with open(pack_path, "r", encoding="utf-8") as f:
                    content_pack = json.load(f)
            except Exception as e:
                logging.error(f"##vso[task.logissue type=error]Error reading {pack_path}: {e}")
                errors = True
                continue

            missing_detections = []
            for detection_rel_path in content_pack.get("detections", []):
                detection_path = os.path.join(detections_dir, detection_rel_path)
                if not os.path.exists(detection_path):
                    missing_detections.append(detection_rel_path)

            if missing_detections:
                logging.error(f"##vso[task.logissue type=error]Missing detections in content pack {pack_filename}:")
                for path in missing_detections:
                    logging.error(f"##vso[task.logissue type=error]   - {path}")
                errors = True
            else:
                logging.info(f"Content pack {pack_filename}: all detections exist.")

    if errors:
        logging.error("##vso[task.logissue type=error]Errors while validating content packs.")
        exit(1)
    else:
        logging.info("All content packs validated successfully.")

def main():
    parser = argparse.ArgumentParser(description="Validate detection paths for all content packs.")
    parser.add_argument("--content_packs_dir", default="content_packs", help="Directory containing content packs")
    parser.add_argument("--detections_dir", default="detections", help="Detections directory")
    args = parser.parse_args()

    validate_packs(args.content_packs_dir, args.detections_dir)

if __name__ == "__main__":
    main()
```

Python

Additionally, the JSON schema for the expected structure of a content pack includes required properties like name, description, version, and detections. Also, minimum length for name and description, as well as expected patterns for version and the detections array is enforced.

```

```

```
{
  "type": "object",
  "required": ["name", "description", "version", "detections"],
  "properties": {
    "name": {
      "type": "string",
      "minLength": 10
    },
    "description": {
      "type": "string",
      "minLength": 20
    },
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$"
    },
    "detections": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[\\w_/]+$"
      },
      "uniqueItems": true,
      "minItems": 1
    }
  },
  "additionalProperties": false
}
```

JSON

The pipeline triggers on changes to any branch and JSON files within the content\_packs directory. Initially, it runs validate\_schema.py to ensure that the content packs files conform to their schema and then validate\_packs.py checks for the existence of detection files referenced in the content packs.

```

```

```
name: Validate Content Packs

trigger:
  branches:
    include:
      - '*'
  paths:
    include:
      - 'content_packs/*.json'

jobs:
- job: ValidateContentPacks
  displayName: "Validate Content Packs"
  steps:
    - checkout: self
    - script: |
        python pipelines/scripts/validate_schema.py --schema pipelines/schemas/content_pack_schema.json --file-dir content_packs --file-regex-filter "\.json"
      displayName: 'Run Content Pack Schema Validation'
    - script: |
        python pipelines/scripts/validate_packs.py --content_packs_dir content_packs --detections_dir detections
      displayName: 'Run Content Pack Validation'

```

YAML

We add the pipeline in the build validation of the main branch and we are now able to detect possible errors with the content pack files.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-51-1024x322.png)

For example, the output of the content pack validation below detected an incorrect format for the version field and a non-existent use case referenced.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-55-1024x98.png)![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-74.png)

## Validation of Repository Structure

As the last step in our validation process, we are going to validate the repository structure.

This script validates a directory tree against predefined structural and naming conventions. It checks for the presence of required top-level directories, such as content\_packs and detections, and ensures that directory and file names conform to a specific pattern using regular expressions. Additionally, it verifies that files within certain directories have files with allowed suffixes. If any discrepancies are found, such as missing directories, unexpected directories, invalid names, or incorrect file suffixes, the script logs errors and exits with a failure status.

```

```

```
import os
import re
import argparse
import logging

# Constants
ALLOWED_ROOT_DIRS = ["content_packs", "detections", "parsers", "pipelines", "tests"]
ALLOWED_DETECTIONS_SUFFIXES = [".json", "_meta.yml"]
ALLOWED_PACKS_SUFFIXES = [".json"]
SKIPPED_DIRS = [".git"]
NAME_PATTERN = re.compile(r"^[a-z0-9_\.]+$")

logger = logging.getLogger(__name__)

def validate_tree(root):
    has_errors = False

    root_dirs = [\
        directory\
        for directory in os.listdir(root)\
        if os.path.isdir(os.path.join(root, directory)) and directory not in SKIPPED_DIRS\
    ]

    # Check for missing root directories
    missing_dirs = list(set(ALLOWED_ROOT_DIRS) - set(root_dirs))
    for missing in missing_dirs:
        logging.error(f"##vso[task.logissue type=error]Missing required root directory: {missing}")
        has_errors = True

    # Check for additional root directories
    extra_dirs = list(set(root_dirs) - set(ALLOWED_ROOT_DIRS))
    for extra in extra_dirs:
        logging.error(f"##vso[task.logissue type=error]Unexpected directory identified: {extra}")
        has_errors = True

    # Walk through the directory tree and validate naming convention and expected files
    for root_dir in root_dirs:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirname = os.path.basename(dirpath)
            if dirname not in SKIPPED_DIRS:
                if not NAME_PATTERN.fullmatch(dirname):
                    logging.error(f"##vso[task.logissue type=error]Invalid directory name: {dirpath}")
                    has_errors = True

                for filename in filenames:
                    if not NAME_PATTERN.fullmatch(filename):
                        logging.error(
                            f"##vso[task.logissue type=error]Invalid filename name: {os.path.join(dirpath, filename)}"
                        )
                        has_errors = True

                if dirpath.startswith("detections"):
                    if dirnames == [] and filenames != []:
                        for filename in filenames:
                            if not any(filename.endswith(suffix) for suffix in ALLOWED_DETECTIONS_SUFFIXES):
                                logging.error(
                                    f"##vso[task.logissue type=error]Invalid file in {dirpath}: {filename} (expected suffixes: {', '.join(ALLOWED_DETECTIONS_SUFFIXES)})"
                                )
                                has_errors = True

                if dirpath.startswith("content_packs"):
                    if dirnames == [] and filenames != []:
                        for filename in filenames:
                            if not any(filename.endswith(suffix) for suffix in ALLOWED_PACKS_SUFFIXES):
                                logging.error(
                                    f"##vso[task.logissue type=error]Invalid file in {dirpath}: {filename} (expected suffixes: {', '.join(ALLOWED_DETECTIONS_SUFFIXES)})"
                                )
                                has_errors = True

    if has_errors:
        logging.error("##vso[task.logissue type=error]Directory tree is invalid.")
        exit(1)
    else:
        logger.info("Directory tree is valid.")

def main():
    parser = argparse.ArgumentParser(description="Validate directory tree structure.")
    parser.add_argument("--root-dir", type=str, help="Path to the repo root directory")
    args = parser.parse_args()

    if not os.path.isdir(args.root_dir):
        logger.error("Provided path is not a directory: %s", args.root_dir)
        exit(1)

    validate_tree(args.root_dir)

if __name__ == "__main__":
    main()
```

Python

The pipeline that leverages the scripts is the following:

```

```

```
name: Validate Repository Structure

trigger:
  branches:
    include:
      - '*'

jobs:
- job: ValidateRepositoryStructure
  displayName: "Validate Repository Structure"
  steps:
    - checkout: self
    - script: |
        python pipelines/scripts/validate_tree.py --root-dir .
      displayName: 'Run Repository Structure Validation'
```

YAML

Once more, we add the pipeline to the build validation and we are able to identify potential issues with the repository.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-80-1024x356.png)

For example in the error below, the validation detected an incorrect file type in the content\_packs directory.

![](https://blog.nviso.eu/wp-content/uploads/2025/08/image-2.png)

## Wrapping Up

In the third part of our blog series, we explored how implementing validation checks across detections, content packs, and the repository structure is essential for maintaining a high-quality and reliable detection library. By enforcing schema conformity, validating query syntax, verifying references and URLs, and ensuring consistent spelling and repository structure, we significantly reduce the risk of errors, catching issues early in the development process, but also promote consistency and throughout the codebase. Setting up automated validation pipelines for these checks is a crucial step toward implementing a Detection-as-Code approach in Detection Engineering.

The next blog of this series will be about automating documentation for our repository.

## References

\[1\] [https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops)

\[2\] [https://json-schema.org](https://json-schema.org/)

\[3\] [https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/key-pipelines-concepts?view=azure-devops)

\[4\] [https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser#build-validation](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops&tabs=browser#build-validation)

\[5\] [https://www.elastic.co/security-labs/streamlining-esql-query-and-rule-validation](https://www.elastic.co/security-labs/streamlining-esql-query-and-rule-validation)

\[6\] [https://github.com/FalconForceTeam/KQLAnalyzer](https://github.com/FalconForceTeam/KQLAnalyzer)

\[7\] [https://github.com/timtim589/KustainerValidation](https://github.com/timtim589/KustainerValidation)

\[8\] [https://github.com/UnauthorizedAccessBV/PowerShell-KQL-Validator](https://github.com/UnauthorizedAccessBV/PowerShell-KQL-Validator)

\[9\] [https://optyx.io/posts/kql-python/](https://optyx.io/posts/kql-python/)

\[10\] [https://pypi.org/project/urlchecker/](https://pypi.org/project/urlchecker/)

\[11\] [https://pypi.org/project/codespell/](https://pypi.org/project/codespell/)

## About the Author

![schat-avatar](https://blog.nviso.eu/wp-content/uploads/2023/02/stamprofile-150x150.png?crop=1)

**Stamatis Chatzimangou**

Stamatis is a member of the Threat Detection Engineering team at NVISO’s CSIRT & SOC and is mainly involved in Use Case research and development.

[LinkedIn](https://www.linkedin.com/in/stamatis-chatzimangou/)

[Twitter](https://twitter.com/_St0pp3r_)

[Github](http://github.com/st0pp3r)

Series Navigation[<< Detection Engineering: Practicing Detection-as-Code – Repository – Part 2](https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/ "<< Detection Engineering: Practicing Detection-as-Code – Repository – Part 2")

### Share this:

- [X](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/?share=twitter&nb=1)
- [Reddit](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/?share=reddit&nb=1)
- [WhatsApp](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/?share=jetpack-whatsapp&nb=1)
- [Email](mailto:?subject=%5BShared%20Post%5D%20Detection%20Engineering%3A%20Practicing%20Detection-as-Code%20-%20Validation%20-%20Part%203&body=https%3A%2F%2Fblog.nviso.eu%2F2025%2F08%2F05%2Fdetection-engineering-practicing-detection-as-code-validation-part-3%2F&share=email&nb=1)

### Like this:

LikeLoading...

- Tagged
- [Detection-as-Code](https://blog.nviso.eu/tag/detection-as-code/)
- [Repository](https://blog.nviso.eu/tag/repository/)
- [Git](https://blog.nviso.eu/tag/git/)
- [Detection](https://blog.nviso.eu/tag/detection/)
- [Detection Engineering](https://blog.nviso.eu/tag/detection-engineering/)
- [Threat Detection](https://blog.nviso.eu/tag/threat-detection/)

## Published by Stamatis Chatzimangou

[View all posts by Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/)

**Published** August 5, 2025August 12, 2025

## One thought on “Detection Engineering: Practicing Detection-as-Code – Validation – Part 3”

1. Pingback: [Detection Engineering: Practicing Detection-as-Code – Validation – Part 3 – Yet Another News Aggregator Channel](https://yanac.hu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/)


### Leave a Reply[Cancel reply](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/\#respond)

Post a Comment

Email me new posts

InstantlyDailyWeekly

Email me new comments

Save my name, email, and website in this browser for the next time I comment.

Comment

Δ

## Discover more from NVISO Labs

Subscribe now to keep reading and get access to the full archive.

Type your email…

Subscribe

[Continue reading](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/#)

[Toggle photo metadata visibility](https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/#)

%d

![](https://blog.nviso.eu/wp-content/plugins/wpfront-scroll-top/includes/assets/icons/1.png)
