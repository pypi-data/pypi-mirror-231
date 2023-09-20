import streamlit.web.cli as stcli


def main():
    # noinspection PyTypeChecker
    stcli.main_run(['ui/ui.py'])


if __name__ == '__main__':
    main()
