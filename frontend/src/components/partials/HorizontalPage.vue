<template>
    <div>
        <slot></slot>
        <div class='arrows' v-show='showArrows'>
            <button class='arrow arrow--next' @click='scroll(1)' v-show='showNextArrow'>Next</button>
            <button class='arrow arrow--prev' @click='scroll(-1)' v-show='showPrevArrow'>Prev</button>
        </div>
    </div>
</template>

<script>
import { EventBus } from './../eventBus.js'
import throttle from './../throttle.js'

export default {
    data () {
        return {
            showArrows: false,
            showNextArrow: true,
            showPrevArrow: true,
        }
    },
    methods: {
        resizeBody () {
            this.showArrows = false
            if (window.innerWidth > 700) {
                if (this.$el.scrollWidth > window.innerWidth) {
                    document.body.style.height = this.$el.scrollWidth + 'px'
                    window.addEventListener('scroll', this.handleScroll)
                    this.showArrows = true
                }
            } else {
                document.body.style.height = 'auto'
                window.removeEventListener('scroll', this.handleScroll)
            }
        },
        handleScroll () {
            const percentageScrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight)
            this.$el.style.transform = 'translateX(-' + (percentageScrolled * (this.$el.scrollWidth - window.innerWidth)) + 'px)'

            this.showPrevArrow = percentageScrolled > 0.05
            this.showNextArrow = percentageScrolled <= 0.95
        },
        scroll (direction) {
            const movement = 450 * direction
            window.scrollTo(0, window.scrollY + movement)
        }
    },
    mounted () {
        this.resizeBody()
        this.handleScroll()
        window.addEventListener('resize', this.resizeBody)
        EventBus.$on('workPhoto:resized', throttle(() => {
            this.resizeBody()
        }, 200))
    },
    destroyed () {
        document.body.style.height = 'auto'
        window.removeEventListener('resize', this.resizeBody)
        window.removeEventListener('scroll', this.handleScroll)
    }
}
</script>

<style scoped lang='scss' src='@/scss/horizontal.scss'></style>
