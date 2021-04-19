FROM continuumio/miniconda3:4.9.2

RUN conda install -y faiss-cpu pytorch torchvision -c pytorch && \
	conda install -y jupyterlab -c conda-forge
