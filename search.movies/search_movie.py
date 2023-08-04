import tkinter as tk
import requests
import json

def search_movie():
    title = movie_entry.get()
    # Replace "YOUR_API_KEY" with your actual OMDb API key
    url = f"http://www.omdbapi.com/?apikey=YOUR_API_KEY&s={title}"

    try:
        response = requests.get(url)
        data = json.loads(response.text)  # Use the json module to parse the JSON response
        if data["Response"] == "True":
            movies_listbox.delete(0, tk.END)
            for movie in data["Search"]:
                movies_listbox.insert(tk.END, f"{movie['Title']} ({movie['Year']})")
        else:
            movies_listbox.delete(0, tk.END)
            movies_listbox.insert(tk.END, "No results found.")
    except requests.exceptions.RequestException:
        movies_listbox.delete(0, tk.END)
        movies_listbox.insert(tk.END, "Connection error. Check your internet.")

# Graphical interface configuration
root = tk.Tk()
root.title("Movie Search")
root.geometry("400x300")

label = tk.Label(root, text="Enter movie title:", font=("Arial", 14))
label.pack(pady=10)

movie_entry = tk.Entry(root, font=("Arial", 12))
movie_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", font=("Arial", 12), command=search_movie)
search_button.pack(pady=10)

movies_listbox = tk.Listbox(root, font=("Arial", 12), selectbackground="#0078D4", selectforeground="white")
movies_listbox.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

root.mainloop()
