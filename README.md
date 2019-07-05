# Cloud Run: Dataset Summaries with Pub/Sub Triggers

<p align="left">
    <img src="img/cloud-run.png" align="middle" alt="Cloud Run."/>
</p>

<br>
This repository provides code for utilizing Cloud Run to run a stateless container that uses Pandas profiling to display the summary statistics from a structured CSV dataset. The CSV file is passed to the container via Pub/Sub messages.