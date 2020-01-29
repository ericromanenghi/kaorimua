<template>
    <div class='photo' :style='styles'></div>
</template>

<script>
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
                    backgroundImage: `url(${this.photo.src})`,
                    width: `${this.photo.ratio / 100 * this.$el.clientHeight}px`,
                }
            } else {
                return {
                    width: '100%',
                    height: '0',
                    paddingBottom: `${100 / this.photo.ratio * 100}%`,
                    backgroundImage: `url(${this.photo.src})`,
                }
            }
            
        },
        resize () {
            this.styles = this.calculateStyles()
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

<style lang='scss' src='@/scss/photo.scss' scoped></style>
