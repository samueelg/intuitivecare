import axios from "axios";

const api = axios.create({
  baseURL: "http://192.168.1.15:8000",
});

export const buscarRegistros = async (termo) => {
  try {
    const response = await api.get(`/buscar`, { params: { termo } });
    return response.data;
  } catch (error) {
    console.error("Erro ao buscar registros:", error);
    return null;
  }
};
