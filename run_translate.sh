#!/bin/bash
source /home/ruslan/develop/GoogleTranslate/venv-translate/bin/activate
export PROJECT_ID=$(/home/ruslan/develop/GoogleTranslate/google-cloud-sdk/bin/gcloud config get-value core/project)
text="$1"
python3 /home/ruslan/develop/GoogleTranslate/app.py "$text" $2 $3

deactivate


