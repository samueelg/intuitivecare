<template>
  <div class="container">
    <h2>Buscar Registros</h2>
    <div class="search-box">
      <input v-model="termo" placeholder="Digite um termo..." @keyup.enter="buscar" />
      <button @click="buscar">Buscar</button>
    </div>

    <div v-if="resultados" class="results">
      <h3>Contas Contábeis</h3>
      <DataTable :value="resultados.contas_contabeis" responsiveLayout="scroll" class="custom-table">
        <Column field="descricao" header="Descrição"></Column>
        <Column field="vl_saldo_final" header="Saldo Final">
          <template #body="slotProps">
            R$ {{ slotProps.data.vl_saldo_final.toFixed(2) }}
          </template>
        </Column>
      </DataTable>

      <h3>Operadoras</h3>
      <DataTable :value="resultados.operadoras" responsiveLayout="scroll" class="custom-table">
        <Column field="razao_social" header="Razão Social"></Column>
        <Column field="cnpj" header="CNPJ"></Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { buscarRegistros } from "@/api/api";
import DataTable from "primevue/datatable";
import Column from "primevue/column";

export default {
  components: {
    DataTable,
    Column,
  },
  setup() {
    const termo = ref("");
    const resultados = ref(null);

    const buscar = async () => {
      resultados.value = await buscarRegistros(termo.value);
    };

    return { termo, buscar, resultados };
  },
};
</script>
