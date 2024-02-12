"""
Interactive ArXiv ML
--------------------

Demonstrating interactive plotting with the ArXiv ML data map.
"""

import numpy as np
import datamapplot


arxivml_data_map = np.load("arxiv_ml_data_map.npy")
arxivml_label_layers = []
for layer_num in range(5):
    arxivml_label_layers.append(
        np.load(f"arxiv_ml_layer{layer_num}_cluster_labels.npy", allow_pickle=True)
    )
arxivml_hover_data = np.load("arxiv_ml_hover_data.npy", allow_pickle=True))

plot = datamapplot.create_interactive_plot(
    arxivml_data_map,
    arxivml_label_layers[0],
    arxivml_label_layers[2],
    arxivml_label_layers[4],
    hover_text = arxivml_hover_data,
    font_family="Playfair Display SC",
    title="ArXiv Machine Learning Landscape",
    sub_title="A data map of papers from the Machine Learning section of ArXiv",
    logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/ArXiv_logo_2022.svg/512px-ArXiv_logo_2022.svg.png",
    on_click="window.open(`http://google.com/search?q=\"{hover_text}\"`)",
    darkmode=True,
)
plot