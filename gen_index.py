import os
import datetime

def create_index_html(folder_path):
    # List all HTML files in the folder, excluding 'index.html'
    files = [f for f in os.listdir(folder_path) if f.endswith('.html') and f.lower() != 'index.html']
    
    # Retrieve creation dates for the files
    files_with_dates = []
    for file in files:
        created = os.path.getctime(os.path.join(folder_path, file))
        files_with_dates.append((file, datetime.datetime.fromtimestamp(created)))

    # Sort files by creation date in reverse order
    files_with_dates.sort(key=lambda x: x[1], reverse=True)
    
    # HTML structure
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index of HTML Files</title>
        <script src="https://cdn.jsdelivr.net/npm/sortablejs@1.14.0/sortable.min.js"></script>
    </head>
    <body>
        <table border="1" id="filesTable">
            <thead>
                <tr>
                    <th>File Name</th>
                    <th>Created Date</th>
                </tr>
            </thead>
            <tbody>
    """
    for file, date in files_with_dates:
        html_content += f"<tr><td><a href='{file}'>{file}</a></td><td>{date.strftime('%Y-%m-%d %H:%M:%S')}</td></tr>"
    
    html_content += """
            </tbody>
        </table>
        <script>
            new Sortable(filesTable, {
                animation: 150,
                multiDrag: true,
                chosenClass: "selected",
                dragClass: "drag",
                dataIdAttr: 'data-id',
                store: {
                    set: function (sortable) {
                        var order = sortable.toArray();
                        localStorage.setItem(sortable.el.id, order.join('|'));
                    },
                    get: function (sortable) {
                        var order = localStorage.getItem(sortable.el.id);
                        return order ? order.split('|') : [];
                    }
                }
            });
        </script>
    </body>
    </html>
    """
    
    # Write HTML to file
    with open(os.path.join(folder_path, 'index.html'), 'w') as file:
        file.write(html_content)

# Example usage
create_index_html('.')  # Uses the current directory

