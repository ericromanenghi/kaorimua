module.exports = {
  devServer: {
    host: '127.0.0.1'
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/admin/'
    : '/'
}