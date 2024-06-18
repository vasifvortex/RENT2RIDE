import { getSingleBikeService } from "./services/bike-service.js";

const bikeContainer = document.querySelector(".bike-detail-wrapper");

// Locate the bike ID from the URL parameters
const url = window.location.pathname; // Gets "/page/123"
const parts = url.split('/'); // Splits into parts
const bikeID = parts[2]; // Access the part that contains the ID


if (!bikeID) {
  console.error("Bike ID not found in the URL parameters.");
} else {
  console.log(`Fetching details for bike ID: ${bikeID}`);
}

// Fetch and bind the bike details
let selectedBike;
const getSingleBike = async (id) => {
  try {
    const data = await getSingleBikeService(id);
    selectedBike = data;
    bindBike(selectedBike);
  } catch (error) {
    console.error("Error fetching bike data:", error);
    handleBikeError('Bike not found.');
  }
};

const baseURL = "/static/assets/";

// Bind bike details to the DOM
function bindBike(bike) {
  if (!bike) {
    console.error("Bike data is null or undefined.");
    return;
  }

  bikeContainer.innerHTML = "";
  const imageBox = document.createElement("div");
  imageBox.classList.add("bike-detail-image-box");
  const image = document.createElement("img");
  image.classList.add("bike-detail-photo");
  image.src = `${baseURL}${bike.image}`;
  image.alt = bike.image;
  imageBox.append(image);
  const bikeDetailInfos = document.createElement("div");
  bikeDetailInfos.classList.add("bikeDetailInfos");
  const individualBikeDetails = document.createElement("div");
  individualBikeDetails.classList.add("individualBikeDetails");
  const h3 = document.createElement("h3");
  h3.classList.add("bike-detail-title");
  h3.textContent = bike.name;
  const p = document.createElement("p");
  p.classList.add("bike-detail-desc");
  p.textContent = bike.comment;
  const span = document.createElement("span");
  span.classList.add("bike-detail-price");
  span.textContent = `${bike.price}AZN`;
  const basketFavouriteButtons = document.createElement("div");
  basketFavouriteButtons.classList.add("basketFavouriteButtons");
  const addBasketButton = document.createElement("button");
  addBasketButton.textContent = "Səbətimə əlavə et";
  addBasketButton.classList.add("addBasketButton");
  addBasketButton.addEventListener("click", () => addToBasket(selectedBike));
  const basketIcon = document.createElement("i");
  basketIcon.classList.add("fa-solid", "fa-cart-shopping");
  addBasketButton.append(basketIcon);
  const addFavouriteButton = document.createElement("button");
  addFavouriteButton.classList.add("addFavouriteButton");
  const favIcon = document.createElement("i");
  favIcon.classList.add("fa-regular", "fa-heart");
  addFavouriteButton.append(favIcon);
  // Appends
  basketFavouriteButtons.append(addBasketButton, addFavouriteButton);
  individualBikeDetails.append(imageBox, h3, p, span);
  bikeDetailInfos.append(individualBikeDetails, basketFavouriteButtons);
  bikeContainer.append(imageBox, bikeDetailInfos);
}

// Function to add product to basket
function addToBasket(product) {
  let basketArray = JSON.parse(localStorage.getItem("basketArray")) || [];
  let existingProduct = basketArray.find((item) => item.id === product.id);
  if (existingProduct) {
    existingProduct.quantity = (existingProduct.quantity || 1) + 1;
  } else {
    product.quantity = 1;
    basketArray.push(product);
  }
  localStorage.setItem("basketArray", JSON.stringify(basketArray));
}

async function initialRenderFunctions() {
  if (bikeID) {
    await getSingleBike(bikeID);
  } else {
    console.error("No bike ID provided in URL.");
  }
}

window.addEventListener("DOMContentLoaded", initialRenderFunctions);
