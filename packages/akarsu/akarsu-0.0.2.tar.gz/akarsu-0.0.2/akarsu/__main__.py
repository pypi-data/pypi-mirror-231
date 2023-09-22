import argparse
import collections
import io

from akarsu.akarsu import Akarsu


def main() -> None:
    parser = argparse.ArgumentParser(
        description="New generation profiler based on PEP 669"
    )
    parser.add_argument("-v", "--version", action="version", version="0.0.1")
    parser.add_argument("-f", "--file", type=str, help="Path to the file")
    args = parser.parse_args()

    if file := args.file:
        with io.open(file) as fp:
            source = fp.read()
        events, counter = Akarsu(source, args.file).profile()
        counted_events = collections.Counter(events).most_common()

        print(f"{'Count':>10}{'Event Type':^20}{'Filename(function)':<50}")
        for event, count in counted_events:
            event_type, file_name, func_name = event
            print(f"{count:>10}{event_type:^20}{f'{file_name}({func_name})':<50}")

        print(f"\nSum of number of events: {counter.total()}")
        for event_type, count in counter.most_common():
            print(f"  {event_type} = {count}")


if __name__ == "__main__":
    main()
