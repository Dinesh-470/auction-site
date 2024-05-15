async function fetchData(auction_name) {
  try {
      let url = '/u/0/api/bids_api/';
      url += auction_name;
      const response = await fetch(url);

      const data = await response.json();
      
      const basePriceElement = document.getElementById('baseprice');
      basePriceElement.innerHTML = data.current_bid;

      const basePriceElement1 = document.getElementById('baseprice1');
      basePriceElement1.innerHTML = '';
      basePriceElement1.innerHTML = data.current_bid ;

      const userBidActivityContainer = document.getElementById('userBidActivity');
      userBidActivityContainer.innerHTML = ''

      for(entry of data['bid']) {
              const userBidActivityDiv = document.createElement('div');
              userBidActivityDiv.classList.add('user_bid_activity');
              const userLink = document.createElement('a');
              userLink.href = `/user/${entry.bidder_name}`;
              const userNameHeader = document.createElement('h3');
              userNameHeader.textContent = entry.bidder_name;
              userLink.appendChild(userNameHeader);
              userBidActivityDiv.appendChild(userLink);
              const userBidPrice = document.createElement('h4');
              userBidPrice.textContent = entry.bid_amount;
              userBidActivityDiv.appendChild(userBidPrice);
              userBidActivityContainer.appendChild(userBidActivityDiv);
            };
            
  } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
  }
}