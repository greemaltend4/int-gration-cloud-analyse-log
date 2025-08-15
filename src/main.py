import json
import boto3
import logging

# Initialiser le client S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Gestionnaire d'événements pour les fichiers téléchargés
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        log_data = download_log_file(bucket, key)
        analysis_results = analyze_logs(log_data)
        report = generate_report(analysis_results)
        save_report(bucket, report)

def download_log_file(bucket, key):
    response = s3_client.get_object(Bucket=bucket, Key=key)
    log_data = response['Body'].read().decode('utf-8')
    return log_data

def analyze_logs(log_data):
    # Exemple d'analyse de logs (ajoutez votre logique ici)
    lines = log_data.split('\n')
    errors = [line for line in lines if 'ERROR' in line]
    return errors

def generate_report(analysis_results):
    report = {'error_count': len(analysis_results), 'errors': analysis_results}
    return report

def save_report(bucket, report):
    report_key = 'reports/error_report.json'
    s3_client.put_object(Bucket=bucket, Key=report_key, Body=json.dumps(report))
    logging.info(f'Rapport sauvegardé: {report_key}')
