import win32com.client as win32
from pathlib import Path

clients = Path(r"C:\Users\Dima_Spektor12\OneDrive\Desktop\Programming\Data Analyst\Excel\Work My Projects\Projects Power Query\Compliance").glob('*.xlsx')

for client in clients:
    xlapp = win32.gencache.EnsureDispatch('Excel.Application')
    print(client)
    xlapp.Visible = False
    wb = xlapp.Workbooks.Open(client)
    wb.RefreshAll()
    xlapp.CalculateUntilAsyncQueriesDone()
    wb.Save()
    wb.Close()

xlapp.Quit()

