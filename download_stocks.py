import nasdaqdatalink
import os

def get_api_key():
    """
    Reads the API key from environment.txt.
    """
    try:
        with open("environment.txt", "r") as f:
            api_key = f.read().strip()
            if not api_key:
                print("Error: environment.txt is empty.")
                return None
            return api_key
    except FileNotFoundError:
        print("Error: environment.txt not found. Please create this file and add your API key to it.")
        return None

def download_stock_data(ticker):
    """
    Downloads historical stock data for a given ticker and saves it to a CSV file.
    """
    # print(f"Downloading data for {ticker}...")
    # try:
    #     # Retrieve the data from Nasdaq Data Link using the WIKI dataset.
    #     data = nasdaqdatalink.get(f"WIKI/{ticker}", collapse="daily")

    #     # Define the output filename.
    #     output_filename = f"{ticker}_stock_data.csv"

    #     # Save the data to a CSV file.
    #     data.to_csv(output_filename)
    #     print(f"Successfully saved data for {ticker} to {output_filename}")

    # except Exception as e:
    #     print(f"Error downloading data for {ticker}: {e}")
    #data = nasdaqdatalink.get(f"WIKI/{ticker}", collapse="daily")



def main():
    """
    Main function to configure API key and download data for all specified tickers.
    """
    api_key = get_api_key()
    if not api_key:
        return

    nasdaqdatalink.ApiConfig.api_key = api_key

    # Define the stock tickers you want to download.
    tickers = ["AAPL", "NVDA"]

    for ticker in tickers:
        download_stock_data(ticker)

if __name__ == "__main__":
    main()
