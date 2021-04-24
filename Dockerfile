FROM continuumio/miniconda3:4.9.2

RUN conda install -y \
		jupyterlab \
		ipywidgets \
		matplotlib \
		scikit-learn \
		imagehash \
		pytorch \
		torchvision \
		faiss-cpu \
	-c conda-forge -c pytorch \
	&& \
	conda clean -i -t -y
