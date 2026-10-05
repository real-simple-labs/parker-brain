# Source pulls

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

The raw reads that the personas and the voice of customer are built from: what the data says before anyone draws a conclusion from it.

## What lives here

- One doc per source: the ad account, ad comments, customer reviews, other reviews, post-purchase surveys, Reddit, brand reputation, and the brand self-echo check (where the brand's own words come back as if they were the customer's).

The prompts that write these docs are the source prompts in `parker-system/prompts/personas/`. The persona profiles and the voice of customer in `../personas/` read from here.

A new brain starts with this folder empty. The build fills it.
