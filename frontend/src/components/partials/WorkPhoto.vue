<template>
    <div class='photo' :style='styles'>
        <img :src='photo.src' alt='' role='presentation'>
    </div>
</template>

<script>
import { EventBus } from './../eventBus.js';

export default {
    props: [ 'photo' ],
    data: function () {
        return {
            styles: '',
        }
    },
    methods: {
        calculateStyles () {
            if (window.innerWidth > 700) {
                return {
                    width: `${this.photo.ratio / 100 * this.$el.clientHeight}px`,
                }
            } else {
                return {
                    width: '100%',
                    height: '0',
                    paddingBottom: `${100 / this.photo.ratio * 100}%`,
                }
            }
            
        },
        resize () {
            this.styles = this.calculateStyles()
            setTimeout(() => {
                EventBus.$emit('workPhoto:resized')
            }, 5)
        }
    },
    mounted () {
        this.resize()
        window.addEventListener('resize', this.resize)
    },
    destroyed () {
        window.removeEventListener('resize', this.resize)
    }
}
</script>

<style lang='scss' src='@/scss/photo.scss'></style>
