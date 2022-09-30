# package imports
from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime as dt
import json
import os
import platform

cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'experience.json')
with open(file_path_in, 'r') as f:
    data = json.load(f)
date_format = '%B %#d, %G' if platform.system() == 'Windows' else '%B %-d, %G'


def create_job_info(job):
    start = dt.strptime(job.get('start_date'), '%m/%d/%Y').strftime(date_format)
    end = dt.strptime(job.get('end_date'), '%m/%d/%Y').strftime(date_format) if job.get('end_date') != '' else ''
    card = dbc.Card(
        [
            html.H4(job.get('title')),
            html.Div(
                [
                    html.Div(
                        [
                            html.Span(job.get('company'), className='fw-bold'),
                            f' - {job.get("location")}'
                        ]
                    ),
                    html.P(f'{start} - {end}'),
                    html.P(job.get('description'))
                ],
                className='ms-3'
            )
        ],
        body=True,
        class_name='border-0'
    )
    return card


jobs = []
for d in data:
    jobs.append(create_job_info(d))
    jobs.append(html.Hr())
jobs.pop()

# set file location
id = 'experience'
layout = dbc.Card(
    [
        html.H2('Work Experience'),
        html.Div(
            jobs
        )
    ],
    id=id,
    body=True,
)
