---
title: 'slant: A Python package for automatically generating experimental placebos'
tags:
  - Python
  - experiments
  - vignette experiments
  - placebo conditions
authors:
  - name: Charles Crabtree^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0001-5144-8671
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: William M. Marx^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0002-0408-0517
    affiliation: 1
#    orcid: 
affiliations:
 - name: Department of Government, Dartmouth College
   index: 1
date: 18 August 2021
bibliography: paper.bib
---

# Summary

Medical and pharmacological researchers have long relied on placebo-controlled studies to isolate and identify the causal effect of a treatment from the causal effect of being treated. In recent years, social scientists have increasingly turned to this study design in survey experiments, particurly vignette-based experiments.  While placebo conditions are now widely used and vitally important to the inferences researchers draw from survey experiments, there’s been little methodological work on either when they should be used or how to create them. `@portervelez:2021` introduce a new approach to creating and selecting placebo conditions - agnostic generation via OpenAI’s GPT-2, a widely used language model. `slant` enables researchers to both reliably and efficiently generate text falling within a predetermined sentiment range using GPT-2.

# Statement of need

`slant` is a Python package for placebo text generation using GPT-2. The widely used text model should not be used to automatically create placebo conditions on its own. As `@crabtreemarx:2021` show, GPT-2 creates very different texts — both in sentiment and substance — depending on group identifiers included in seed phrases. This is problematic for all those who might wish to use the tool in creating placebos for experiments, regardless of why the language model performs this way and whether they would use these phrases in their own work. 

Our tool, `slant`, enables researchers to both reliably and efficiently generate text falling within a predetermined sentiment range using GPT-2. Outside of fast, sentiment-bounded text generation, `slant` provides a simple interface to our fastVADER algorithm, which reproduces results of Hutto and Gilbert’s VADER tool several orders of magnitude faster. Finally, `slant` includes a dictionary of potentially biasing words, against which it checks generated text against, while also recognizing combinations of adjectives and proper nouns for researchers to manually verify, helping to minimize the possibility of generating text incongruous with commonly-known fact.

`slant` was designed to be used by researchers who create and implement text-based survey experiments, particularly those that rely on vignettes. We expect that it will be particularly useful to researchers doing work in substantive areas where the bias contained and perpetuated by GPT-2 is most problematic, such as in race and ethnic politics.

# Acknowledgements

We acknowledge advice from Matt Golder and Sona Golder during the genesis of this project.

# References
