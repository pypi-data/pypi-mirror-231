# htcondor-queue-poller

Script to check whether job are queued in the HTCondor. Can be used in combination with the `Stopper` decorator of the [`cobald-hep-plugins`](https://github.com/MatterMiners/cobald-hep-plugins) package to force the demand of `COBalD` to be Zero as long as no jobs are handled by HTCondor.