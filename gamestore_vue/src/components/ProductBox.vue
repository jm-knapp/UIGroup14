<template>
        <div class="column is-3">
            <div class="box">
                <figure class="image mb-4">
                    <img v-bind:src="product.get_thumbnail">
                </figure>
            
                <h3 class="is-size-4">{{  product.name }}</h3>
                <p class="is-size-6 has-text-grey">
                    <span v-if="product.salePercentAsDeci > 0" class="has-text-danger">
                        <span class="strikethrough">${{ product.price }}</span>
                        <span> ${{ salePrice.toFixed(2) }}</span>
                    </span>
                    <span v-else>${{ product.price }}</span>    
                </p>
                <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4" :aria-label="'View ' + product.name + ' details'">View details</router-link>

          
            </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ProductBox',
    props: {
        product: Object
    },
    computed: {
        salePrice(){
            return this.product.price * (1-this.product.salePercentAsDeci)
        },
    },
    methods: {
        generateDetailsLabel(name){
            return 'View ${name} details'
        }
    }
}

</script>

<style scoped>
  .image{
      margin-top: -1.25rem;
      margin-left: -1.25rem;
      margin-right: -1.25rem;
  }
  .strikethrough{
    text-decoration: line-through;
    color: #808080;
  }


</style>
