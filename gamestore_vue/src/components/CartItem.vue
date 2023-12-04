<template>
    <tr>
        <td class="has-text-left"><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td class="has-text-left">${{ item.product.price }}</td>
        <td class="has-text-left">{{ item.product.salePercentAsDeci !==0 ? (item.product.salePercentAsDeci*100) + '%' : '0%' }}</td>
        <td class="has-text-left">
            <span class="sr-only">Quantity: </span>
            {{ item.quantity }}
            <button @click="decrementQuantity(item)" class="is-size-4 has-text-weight-bold" aria-label="Decrease quantity of item" title="decrease quantity button">
                <span class="extendMinus" aria-hidden="true">-</span>
            </button>
            <button @click="incrementQuantity(item)" class="is-size-4 has-text-weight-bold" aria-label="Increase quantity of item" title="increase quantity button">
                <span class="extendMinus" aria-hidden="true">+</span>
            </button>
        </td>
        <td class="has-text-left">${{ getItemTotal(item).toFixed(2) }}</td>
        <td class="has-text-left"><button class="delete" @click="removeFromCart(item)" aria-label="Remove Item"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        //Can probably modify the below for discounts
        getItemTotal(item) {
            if(item.product.salePercentAsDeci > 0){
                return item.quantity * item.product.price * (1-item.product.salePercentAsDeci)
            }else{
                return item.quantity * item.product.price
            }
            
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
                notificationAlert(this.item.product.name + ' removed from cart.')
            }

            this.updateCart()
            notificationAlert('decreased quantity of ' + this.item.product.name + ' by one.')
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
            notificationAlert('increased quantity of ' + this.item.product.name + ' by one.')
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
            notificationAlert(this.item.product.name + ' removed from cart.')
        },
    },
}

function notificationAlert(message){
    let liveRegion = document.getElementById('live-region');
    liveRegion.textContent = message;
    liveRegion.setAttribute('aria-live', 'assertive');
    liveRegion.focus();
}
</script>

<style lang="scss">
    .extendMinus::before{
        content: "\00a0";
        display: inline-block;
    }
    .extendMinus::after{
        content: "\00a0";
    }

    .sr-only{
        position: absolute;
        width: 1px;
        height: 1px;
        margin: -1px;
        padding: 0;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        border: 0;
    }
</style>