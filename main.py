import os
from dotenv import load_dotenv
from vcenterapi import Vcenterapi


def main():
    load_dotenv()

    consulta = Vcenterapi()
    consulta.loggin()
    consulta.get_header()
    #print(consulta.getAllVm())
    consulta.getVm("vm-102")
    


if __name__ == "__main__":
    main()