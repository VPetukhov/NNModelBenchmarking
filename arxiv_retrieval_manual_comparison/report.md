##

В моих бенчмарках использовались только абстракты (без заголовков)


 
## Manual Observations

(I compare only e5 and bm25, without colbert)

- When searching query is an abbreviation (see `keyword_query_GAN` and `keyword_query_unet`) both bm25 and e5 fail to grasp the meaning of 
the abbreviation and return results based on the occurrence of the abbreviation in the abstract.

- Broad keyword queries seem to return vaguely related results, but neither bm25 nor e5 return Google-level quality 
results in terms of usefullness of those results to answering the question of "what is `[query]`?", 
which is the fault of the data in the first place, and not of the retrieval method. 
However, it feels like e5 is slightly better than bm25 in this regard 
(at least in the case of `keyword_query_graph_convolutional_neural_network` and `keyword_query_reinforcement_learning`), 
but, once again, it may be the lack of documents that answer the question "what is `[query]`?" directly in the data.
)

- For narrow queries both models are capable of retrieving relevant papers (and the retrieved abstracts are way better
at answering the narrow queries, than the broad queries, because (i think) the narrow queries ask for specific things which can be found in 
the abstracts, and not for a general explanation of the terms of the query). However, both models fail to put the 
most relevant paper at the top of their results:
  - `narrow_keyword_query_kernel_augmentation_for_computed_tomography`: the relevant paper is `Zero-Shot Domain Adaptation 
in CT Segmentation by Filtered Back Projection Augmentation`, which is ranked 4th(bm25) and 3rd(e5)
  - `narrow_keyword_query_calibrated_probabilities_on_BERT_classification`: the most relevant paper appears to be
`Calibration of Pre-trained Transformers`, which is ranked 7th(bm25) and 6th(e5).

- Additionally, for the narrow queries it looks like e5 is better at determining which parts of the query are more
important (see `narrow_keyword_query_prompt_engineering_via_chain_of_thoughts`,
`narrow_keyword_query_kernel_augmentation_for_computed_tomography` and
`narrow_keyword_query_calibrated_probabilities_on_BERT_classification`)

- 