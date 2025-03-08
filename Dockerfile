FROM continuumio/miniconda3

WORKDIR /app

COPY environment-docker.yml /app/environment.yml

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q && \
    apt-get upgrade -y && \
    apt-get install -q -y --no-install-recommends \
        locales-all \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN conda env create -f /app/environment.yml \
    && conda clean --all -f -y \
    && rm -rf /opt/conda/pkgs/*

RUN echo "source activate uoc" > ~/.bashrc

ENV PATH /opt/conda/envs/uoc/bin:$PATH