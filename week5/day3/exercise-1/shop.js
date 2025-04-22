const products = require('./products');
function findProductByName(productName) {
    const product = products.find(p => p.name.toLowerCase() === productName.toLowerCase());
    if (product) {
        console.log("Produit trouvé:", product);
    } else {
        console.log(`Aucun produit trouvé avec le nom: ${productName}`);
    }
}
findProductByName("Laptop");
findProductByName("Desk Chair");
findProductByName("Toaster");