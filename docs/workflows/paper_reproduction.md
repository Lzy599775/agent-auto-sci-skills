# Paper Reproduction Workflow

## Reproduction types

- `EXACT_REPLICATION`: same data, code/method, parameters, and target outputs where available.
- `METHOD_REPRODUCTION`: same method applied to available inputs, without claiming exact result identity.
- `PUBLIC-DATA_EQUIVALENT_REPRODUCTION`: analogous public data substitute used transparently.
- `CONCEPTUAL_REIMPLEMENTATION`: independent implementation of the reported idea or algorithm.

Never label substitute-data or conceptual work as exact replication.

## Pipeline

`paper -> method extraction -> data inventory -> availability audit -> exact versus substitute data -> environment -> minimal reproduction -> validation -> difference attribution -> optional extension`

## Procedure

1. Verify the target paper, version, supplements, code, data, and licenses.
2. Extract method steps, equations, parameters, preprocessing, validation, and output definitions.
3. Inventory required versus available data and software.
4. Declare the reproduction type before implementation.
5. Record environment, dependencies, versions, seeds, and hardware only when relevant.
6. Implement the smallest end-to-end result that tests the central claim.
7. Validate intermediate artifacts, not only the final metric or figure.
8. Attribute differences to data, preprocessing, parameterization, implementation, stochasticity, or undocumented choices.
9. Separate replication findings from innovation extensions.

## Outputs

- Reproduction plan.
- Data and availability inventory.
- Environment and parameter record.
- Validation comparison.
- Difference-attribution report.
- Honest reproduction classification.
