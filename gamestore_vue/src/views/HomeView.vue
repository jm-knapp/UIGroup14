<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to the Game Item Shop!
        </p>
        <p class="subtitle">
          Best in game item shop around! Give us your money!
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

        <ProductBox
          v-for="product in latestProducts"
          v-bind:key="product.id"
          v-bind:product="product" />

      
    </div>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Products On Sale</h2>
      </div>

        <ProductBox
          v-for="product in onSaleProducts"
          v-bind:key="product.id"
          v-bind:product="product" />

      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
  name: 'HomeView',
  data() {
    return{
      latestProducts: [],
      onSaleProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted(){
    this.getLatestProducts()
    this.getOnSaleProducts()

    document.title = ' Homepage <> Game Item Shop!'
  },
  methods: {
    async getLatestProducts(){
      this.$store.commit('setIsLoading', true)

      await axios
      .get('/api/v1/latest-products/')
      .then(response => {
        this.latestProducts = response.data
      })
      .catch(error => {
        console.log(error)
      })

      this.$store.commit('setIsLoading', false)
    },
    async getOnSaleProducts(){
      axios.get('/api/v1/on-sale/')
      .then(response =>{
        this.onSaleProducts = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }


  }
}
</script>