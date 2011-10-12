#!/usr/bin/env python
#
# form_processor.py
# Python module for converting HTML form inputs into dictionaries
# By Brandon Smith (brandon.smith@studiobebop.net)
#
import BeautifulSoup

def parse_forms(page_url, page_content):
    soup = BeautifulSoup.BeautifulSoup(page_content)

    forms = []
    for form in soup.findAll("form"):
        form_action = form["action"]
        form_data = {}
        for input in form.findAll("input"):
            if not input.has_key("name"):
                continue
            try:
                input_name = input["name"]
            except:
                print "#" * 75
                print input
                print "#" * 75
                exit()
            if input.has_key("value"):
                input_value = input["value"]
            else:
                input_value = ""
            form_data[input_name] = input_value
        form = {"action": form_action, "inputs": form_data}
        forms.append(form)

    return forms

