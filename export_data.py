from google.colab import auth
from googleapiclient.discovery import build

auth.authenticate_user()

def write_to_sheet(df, sheet_id, sheet_range):

   # Create the service client
   service = build('sheets', 'v4')

   # Clear the existing values in the sheet
   service.spreadsheets().values().clear(
       spreadsheetId=sheet_id, range=sheet_range).execute()

   # Write the DataFrame to the sheet
   values = df.values.tolist()
   body = {
       'values': values
   }
   result = service.spreadsheets().values().update(
       spreadsheetId=sheet_id, range=sheet_range,
       valueInputOption='USER_ENTERED', body=body).execute()
   print('{0} cells updated.'.format(result.get('updatedCells')))

# The existing sheet we want to overwrite in Drive
sheet_id = '1KMhP6fn_4prOEYs284vBESojTH0J0hPkdwNQRb2EuC8'
sheet_range = 'project_sample_data!A2:G'

# Execute the overwrite with data outputted from models in df (prediction_data)
write_to_sheet(prediction_data[['week','player','team','position','standard_points',
                           'half_ppr_points','ppr_points']], sheet_id, sheet_range)
