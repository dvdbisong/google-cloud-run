# Cloud Run: Dataset Summaries with Pub/Sub Triggers

<!-- <p align="left">
    <img src="img/docker.png" align="middle" alt="Docker." height=20% width=20%/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="img/kubernetes.jpg" align="middle" alt="Kubernetes." height=20% width=20%/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="img/kubeflow.jpg" align="middle" alt="Kubeflow." height=20% width=20%/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="img/gcp.png" align="middle" alt="Google Cloud Platform." height=20% width=20%/>
</p>

<br> -->
This repository provides code for utilizing Cloud Run to run a stateless container that uses Pandas profiling to display the summary statistics from a structured CSV dataset. The CSV file is passed to the container via Pub/Sub messages.