import os
from synapsis import Synapsis


def on_after_login(hook):
    for name, default, attr in [
        ('SYNTOOLS_MULTI_THREADED', 'False', 'multi_threaded'),
        ('SYNTOOLS_USE_BOTO_STS_TRANSFERS', 'False', 'use_boto_sts_transfers')
    ]:
        env_value = os.environ.get(name, default).lower() == 'true'
        setattr(Synapsis.Synapse, attr, env_value)


Synapsis.hooks.after_login(on_after_login)
