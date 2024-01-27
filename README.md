# Project Template for BioInfoX Tools

This project is a Python sketch project for BioInfoX Tools.

## Getting Started

### Prerequisites

-   Python 3.8+
-   pip

### Installation

1. Clone the repository
   `git clone https://github.com/bioinfox/tool-template.git`

2. Navigate into the cloned repository
   `cd backend`

3. Install the required packages

    - `make install`
    - or `pip install -r requirements.txt`

4. Start the server
    - `make run`

## Development

1. Add a module in `src/tools`, you may refer to `holiday.py` in the `tools`

2. Add `class YourAwesomeTool(Tool)` as a subclass of the `Tool` in `from ..type import Tool`

3. Describe the `name`, `name_for_human`, `description`, and `arguments` properties.

4. Implement the `run` function. Notice: the `args` parameter in `run` is a `str` which should be well-formatted from a valid json object.

5. Write test cases in the `tests`, and run the tests with `make test`.

## API Endpoints

You may find the API endpoints at `http://YOUR_SERVER_IP:PORT/docs` when you start the server with `make run`.

## Contributing

## License
