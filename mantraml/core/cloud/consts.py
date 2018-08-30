DEFAULT_SH_SCRIPT = '''#!/bin/bash
        source /home/ubuntu/anaconda3/bin/activate tensorflow_p36
        pip install -r requirements.txt --quiet
        pip install mantraml --quiet
        mantra train %s --dataset %s %s'''

DEFAULT_SH_SCRIPT_VERBOSE = '''#!/bin/bash
        source /home/ubuntu/anaconda3/bin/activate tensorflow_p36
        pip install -r requirements.txt
        pip install mantraml
        mantra train %s --dataset %s %s'''

DEFAULT_SH_TASK_SCRIPT = '''#!/bin/bash
        source /home/ubuntu/anaconda3/bin/activate tensorflow_p36
        pip install -r requirements.txt --quiet
        pip install mantraml --quiet
        mantra train %s --dataset %s --task %s %s'''

DEFAULT_SH_TASK_SCRIPT_VERBOSE = '''#!/bin/bash
        source /home/ubuntu/anaconda3/bin/activate tensorflow_p36
        pip install -r requirements.txt
        pip install mantraml
        mantra train %s --dataset %s --task %s %s'''

MANTRA_DEVELOPMENT_TAG_NAME = 'mantra dev'