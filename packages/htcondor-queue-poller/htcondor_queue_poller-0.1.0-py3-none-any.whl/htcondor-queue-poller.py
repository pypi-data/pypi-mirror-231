#!/bin/python3

import argparse
import htcondor


def get_commandline_arguments():
    parser = argparse.ArgumentParser(
        prog="htcondor-queue-poller", description="Get number of jobs in HTCondor queue"
    )
    parser.add_argument(
        "-p", "--pool", dest="pool", help="Pool to list Schedds", default=""
    )
    parser.add_argument(
        "-c",
        "--constraint",
        help="Additional constraint the jobs need to fulfill",
        default=True,
    )

    return parser.parse_args()


def get_schedds(collector):
    for schedd in collector.locateAll(htcondor.DaemonTypes.Schedd):
        yield htcondor.Schedd(schedd)


def get_number_of_jobs(schedd, constraint=True):
    try:
        return len(schedd.query(constraint=constraint))
    except htcondor.HTCondorIOError:
        return 0


def main():
    args = get_commandline_arguments()

    collector = htcondor.Collector(pool=args.pool)

    number_of_jobs = sum(
        get_number_of_jobs(schedd, constraint=args.constraint)
        for schedd in get_schedds(collector)
    )

    print(number_of_jobs)


if __name__ == "__main__":
    main()
