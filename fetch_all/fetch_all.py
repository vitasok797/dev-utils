import subprocess
import sys
from pathlib import Path


def fetch_dir(target_dir: Path) -> None:
    print(f'Fetching "{target_dir.name}"... ', end='')

    args = ['git', 'fetch', '--all']

    try:
        subprocess.run(
                args,
                cwd=target_dir,
                capture_output=True,
                shell=True,
                check=True,
                )
        print('OK')
    except subprocess.CalledProcessError:
        print('error')
        sys.exit(1)


def main() -> None:
    work_dir = Path(__file__).parent
    dir_items = work_dir.glob('*')
    dirs = [item for item in dir_items if item.is_dir()]

    for target_dir in dirs:
        fetch_dir(target_dir)

    print('Done')


if __name__ == '__main__':
    main()
