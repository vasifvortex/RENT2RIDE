const BASE_URL = "http://127.0.0.1:8000";

export default class ApiRequest {
  async get(endpoint) {
    return await fetch(`${BASE_URL}${endpoint}`);
  }

  async post(endpoint, data) {
    return await fetch(`${BASE_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  }
  async put(endpoint, data) {
    return await fetch(`${BASE_URL}${endpoint}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  }

  async delete(endpoint) {
    return await fetch(`${BASE_URL}${endpoint}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
  }
}
