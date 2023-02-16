import os
import pandas as pd
from abc import abstractmethod
from itertools import chain
from typing import Iterable, Dict, IO


class BaseSearchEngine:
    @abstractmethod
    def index(self, dataset: pd.DataFrame, ids_column_name: str = 'id', abstract_column_name: str = 'abstract'):
        pass

    @abstractmethod
    def retrieve(self, query: str, amount: int) -> Iterable[str]:
        pass

    # @abstractmethod
    # def retrieve_scores(self, query: str, amount: int) -> Dict[str, float]:
    #     pass


def benchmark(dataset_df: pd.DataFrame, search_engine: BaseSearchEngine, path_to_result_dir: str, topk: int = 10):
    if not os.path.exists(path_to_result_dir):
        os.mkdir(path_to_result_dir)

    keyword_queries = [
        "bayesian neural networks",
        "transformers",
        "reinforcement learning",
        "attention is all you need",
        "unet",
        "vanishing gradient",
        "statistical methods",
        "explainable machine learning",
        "prompt engineering",
        "graph convolutional neural network",
        "generative adversarial network",
        "GAN"
    ]
    narrow_keyword_queries = [
        "calibrated probabilities on BERT classification",
        "kernel augmentation for computed tomography",
        "prompt engineering via chain of thoughts",
        "review of computed tomography segmentation",
        "model training on multiple GPUs",
        "transformers interpretability"
    ]
    qna_free_text_queries = [
        "how to scale transformer training to TPU cloud",
        "how to improve quality of image segmentation",
        "how to solve the vanishing gradient problem",
        "how to efficiently deploy large models to production",
        "how to benchmark large language models",
        "what are the strategies for adversarial attacks on computer vision models",
        "how to train models",
        "when will we solve AGI",
        "how to generate a picture with ai"
    ]

    def write_results(file: IO, result: Iterable[str]):
        for i, doc_id in enumerate(result):
            _title = list(dataset_df[dataset_df['id'] == doc_id]['title'])[0]
            _abstract = list(dataset_df[dataset_df['id'] == doc_id]['abstract'])[0].replace('\n', ' ')
            file.write(f"{i + 1}: \n")
            file.write(f"Title: {_title}\n")
            file.write(f"Abstract:\n{_abstract}\n\n")

    for query, query_type in chain(zip(keyword_queries, ("keyword_query" for q in keyword_queries)),
                                   zip(narrow_keyword_queries,
                                       ("narrow_keyword_query" for q in narrow_keyword_queries)),
                                   zip(qna_free_text_queries, ("qna_free_text_query" for q in qna_free_text_queries))):
        result = search_engine.retrieve(query, topk)
        with open(f"{path_to_result_dir}/{query_type}_{'_'.join(query.split())}", "w") as file:
            file.write(f"Query:\n{query}\n\nResults:\n")
            write_results(file, result)

    similiarity_queries = {
        "Unet": "There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU. The full implementation (based on Caffe) and the trained networks are available at this http URL",
        "Attention is all you need": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.",
        "Go": "The game of Go has long been viewed as the most challenging of classic games for artificial intelligence owing to its enormous search space and the difficulty of evaluating board positions and moves. Here we introduce a new approach to computer Go that uses ‘value networks’ to evaluate board positions and ‘policy networks’ to select moves. These deep neural networks are trained by a novel combination of supervised learning from human expert games, and reinforcement learning from games of self-play. Without any lookahead search, the neural networks play Go at the level of state-of-the-art Monte Carlo tree search programs that simulate thousands of random games of self-play. We also introduce a new search algorithm that combines Monte Carlo simulation with value and policy networks. Using this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other Go programs, and defeated the human European Go champion by 5 games to 0. This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away.",
        "BERT": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).",
        "AlexNet": "We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art. The neural network, which has 60 million parameters and 650,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and three fully-connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of the convolution operation. To reduce overfitting in the fully-connected layers we employed a recently-developed regularization method called “dropout” that proved to be very effective. We also entered a variant of this model in the ILSVRC-2012 competition and achieved a winning top-5 test error rate of 15.3%, compared to 26.2% achieved by the second-best entry.",
        "ResNet": "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers---8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers. The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.",
        "Dropout": "Deep neural nets with a large number of parameters are very powerful machine learning systems. However, overfitting is a serious problem in such networks. Large networks are also slow to use, making it difficult to deal with overfitting by combining the predictions of many different large neural nets at test time. Dropout is a technique for addressing this problem. The key idea is to randomly drop units (along with their connections) from the neural network during training. This prevents units from co-adapting too much. During training, dropout samples from an exponential number of different 'thinned' networks. At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. This significantly reduces overfitting and gives major improvements over other regularization methods. We show that dropout improves the performance of neural networks on supervised learning tasks in vision, speech recognition, document classification and computational biology, obtaining state-of-the-art results on many benchmark data sets."
    }

    for paper_name, abstract in similiarity_queries.items():
        result = search_engine.retrieve(abstract, topk)
        with open(f"{path_to_result_dir}/similiarity_queries_{'_'.join(paper_name.split())}", "w") as file:
            abstract_str = abstract.replace('\n', ' ')
            file.write(f"Similiarity query for paper {paper_name}\nQuery:\n{abstract_str}\n\nResults:\n")
            write_results(file, result)