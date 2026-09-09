# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, "%Y-%m-%d")
    entry.description = description
    entry.change = change
    return entry


def generate_header_row(data):

    date_column = data["date"] + data["date_space"] * " "
    description_column = data["description"] + data["description_space"] * " "
    change_column = data["change"] + data["change_space"] * " "

    return f"{date_column}{description_column}{change_column}"


def generate_entry_date(entry, locale):

    month = f"{entry.date.month:02d}"
    day = f"{entry.date.day:02d}"
    year = f"{entry.date.year:04d}"

    if locale == "en_US":
        return f"{month}/{day}/{year} | "

    return f"{day}-{month}-{year} | "


def generate_entry_description(entry):
    description_length = len(entry.description)

    if description_length > 25:
        return f"{entry.description[:22]}... | "

    return f"{entry.description}{(25-description_length) * " "} | "


def generate_change_cents(entry):

    change_cents = abs(entry.change) % 100
    return f"{change_cents:02d}"


def generate_entry_change(entry, currency, locale):
    change_str = "$" if currency == "USD" else "€"

    if locale == "nl_NL":
        change_str += " "

    change_currency = abs(int(entry.change / 100.0))

    currency_parts = []

    while change_currency > 0:
        currency_parts.insert(0, str(change_currency % 1000))
        change_currency = change_currency // 1000

    if len(currency_parts) == 0:
        change_str += "0"
    else:
        while True:
            change_str += currency_parts.pop(0)
            if len(currency_parts) == 0:
                break
            change_str += "," if locale == "en_US" else "."

    change_str += "." if locale == "en_US" else ","
    change_str += generate_change_cents(entry)

    change_str = (
        f"{f"({change_str})" if entry.change < 0 else change_str + " "}"
        if locale == "en_US"
        else f"{f"{change_str[0]} -{change_str[2:]}" if entry.change < 0 else change_str} "
    )

    return " " * (13 - len(change_str)) + change_str


def find_next_entry_in_order(entries):

    entries.sort(
        key=lambda entry: (
            entry.date,
            entry.change,
            entry.description,
        )
    )
    return entries.pop(0)


def generate_table(header_data, entries, locale, currency):
    table = generate_header_row(header_data)

    while len(entries) > 0:
        table += "\n"

        # Find next entry in order
        entry = find_next_entry_in_order(entries)

        # Write entry date to table
        table += generate_entry_date(entry, locale)

        # Write entry description to table
        # Truncate if necessary
        table += generate_entry_description(entry)

        # Write entry change to table
        table += generate_entry_change(entry, currency, locale)

    return table


def format_entries(currency, locale, entries):

    header_data = (
        {
            "date": "Date",
            "date_space": 7,
            "description": "| Description",
            "description_space": 15,
            "change": "| Change",
            "change_space": 7,
        }
        if locale == "en_US"
        else {
            "date": "Datum",
            "date_space": 6,
            "description": "| Omschrijving",
            "description_space": 14,
            "change": "| Verandering",
            "change_space": 2,
        }
    )

    return generate_table(header_data, entries, locale, currency)
