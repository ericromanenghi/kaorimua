<template>
    <div>
        <div class='work'>
            <div class='work__list' ref='list'>
                <div class='work__item work__item--menu'>(menu)</div>
                <div class='work__item'>Box 1</div>
                <div class='work__item'>Box 2</div>
                <div class='work__item'>Box 3</div>
                <div class='work__item'>Box 4</div>
                <div class='work__item'>Box 5</div>
                <div class='work__item'>Box 6</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        resizeBody () {
            document.body.style.height = this.$refs.list.scrollWidth + 'px'
        },
        handleScroll () {
            const percentageScrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight)
            this.$refs.list.style.transform = 'translateX(-' + (percentageScrolled * (this.$refs.list.scrollWidth - window.innerWidth)) + 'px)'
        }
    },
    mounted () {
        this.resizeBody()
        window.addEventListener('resize', this.resizeBody)
        window.addEventListener('scroll', this.handleScroll)
    },
    destroyed () {
        document.body.style.height = 'auto'
        window.removeEventListener('resize', this.resizeBody)
        window.removeEventListener('scroll', this.handleScroll)
    }
}
</script>

<style scoped>
.work {
    background: #efefef;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
}
.work__list {
    display: flex;
    flex-wrap: nowrap;
}
.work__item {
    flex: 0 0 auto;
    height: 100vh;
    width: 400px;
}
.work__item--menu {
    visibility: hidden;
    width: 300px;
}
.work__item:nth-child(2n) {
    background: rgba(0, 0, 0, .05);
}
</style>
