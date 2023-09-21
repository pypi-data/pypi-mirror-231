# PRObs ontology conversion module

This module contains scripts for converting an ontology to Datalog rules and bundling additional required facts together.

These scripts are compatible with [RDFox](https://www.oxfordsemantic.tech) version 6.3a.

## Running the RDFox scripts

This module reads the ontology definitions and data, and splits them into data (`probs_ontology_data`) and Datalog rules (`probs_ontology_rules`).

To run the module:

```sh
RDFox sandbox <root> scripts/ontology-conversion/master
```

where `<root>` is the path to this folder.

The converted data and rules will be written to `data/`.

## Using probs-runner

Using [probs-runner](https://github.com/probs-lab/probs-runner), this module can be run using the `probs_convert_ontology` function.
