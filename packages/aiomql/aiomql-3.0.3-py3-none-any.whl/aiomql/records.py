"""This module contains the Records class, which is used to read and update trade records from csv files."""

import asyncio
from datetime import datetime
from pathlib import Path
import csv

from .history import History
from .core import Config


class Records:
    """This utility class read trade records from csv files, and update them based on their closing positions.

    Attributes:
        config: Config object
        records_dir(Path): Path to directory containing record of placed trades, If not given takes the default
            from the config
    """
    config: Config = Config()
    
    def __init__(self, records_dir: Path = ''):
        """Initialize the Records class.
        Keyword Args:
            records_dir (Path): Path to directory containing record of placed trades.

        """
        self.records_dir = records_dir or self.config.records_dir

    async def get_records(self):
        """Get trade records from records_dir folder

        Yields:
            files: Trade record files
        """
        for file in self.records_dir.iterdir():
            if file.is_file() and file.name.endswith('.csv'):
                yield file

    async def read_update(self, file: Path):
        """Read and update trade records

        Args:
            file: Trade record file
        """
        fr = open(file, mode='r', newline='')
        reader = csv.DictReader(fr)
        rows = [row for row in reader]
        rows = await self.update_rows(rows)
        fr.close()
        fw = open(file, mode='w', newline='')
        writer = csv.DictWriter(fw, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        fw.close()

    async def update_rows(self, rows: list[dict]) -> list[dict]:
        """Update the rows of entered trades in the csv file with the actual profit.

        Args:
            rows: A list of dictionaries from the dictionary writer object of the csv file.

        Returns:
            list[dict]: A list of dictionaries with the actual profit and win status.
        """
        start = float(min(rows, key=lambda r: r['time'])['time'])
        end = datetime.utcnow().timestamp()
        his = History(date_from=start, date_to=end)
        await his.init(orders=False)
        deals = {str(deal.position_id): deal.profit for deal in his.deals}
        for row in rows:
            if (deal := row['order']) in deals:
                profit = deals[deal]
                row.update(actual_profit=profit, win=profit > 0)
        return rows

    async def update_records(self):
        """Update trade records in the records_dir folder."""
        records = [self.read_update(record) async for record in self.get_records()]
        await asyncio.gather(*records)

    async def update_record(self, file: Path | str):
        """Update a single trade record file."""
        await self.read_update(file)
