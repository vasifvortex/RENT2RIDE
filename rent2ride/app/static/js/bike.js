// import { BIKES } from "./data.js";
import { getSingleBikeService } from "../services/bike-service.js";

const bikeContainer = document.querySelector(".bike-detail-wrapper");

//locateToIndividualBikePage
const params = new URLSearchParams(window.location.search);
const bikeID = params.get("id");
// const selectedBike = BIKES.find((bike) => bike.title === bikeTitle);
let selectedBike;

const getSingleBike = async (id) => {
  try {
    const data = await getSingleBikeService(id);
    selectedBike = data;
  } catch (error) {
    console.log(error);
  }
};
const baseURL = "../assets/";
//bind bike
function bindBike(bike) {
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
  //appends
  basketFavouriteButtons.append(addBasketButton, addFavouriteButton);
  individualBikeDetails.append(imageBox,h3, p, span);
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
  await getSingleBike(bikeID);
  bindBike(selectedBike);
}
window.addEventListener("DOMContentLoaded", initialRenderFunctions);
