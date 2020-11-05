import json

def prettyPrintJSON(obj, indent=1):
  print(json.dumps(obj, indent))

def printTable(keys, rows):
  table = [[key] + [str(row[key]) for row in rows] for key in keys]
  columnWidths = [max(len(row) for row in column) for column in table]
  numColumns = len(keys)
  lineLength = sum(columnWidths) + 3 * numColumns

  print(*[k.rjust(columnWidths[i]) for i, k in enumerate(keys)], sep=' | ')
  print(lineLength * '=')

  for row in rows:
    values = [str(row[k]) for k in keys]
    print(*[v.rjust(columnWidths[i]) for i, v in enumerate(values)], sep=' | ')
