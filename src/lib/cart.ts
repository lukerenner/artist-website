export interface CartItem {
    id: string;
    qty: number;
}

export interface Cart {
    items: CartItem[];
}

export interface Product {
    id: string;
    name: string;
    price: number;
    currency: string;
}

const STORAGE_KEY = 'bonnie_cart';

// Helper to get cart from storage
function loadCart(): Cart {
    if (typeof localStorage === 'undefined') return { items: [] };
    const stored = localStorage.getItem(STORAGE_KEY);
    return stored ? JSON.parse(stored) : { items: [] };
}

// Helper to save cart and dispatch event
function saveCart(cart: Cart) {
    if (typeof localStorage !== 'undefined') {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
        // Dispatch custom event for UI updates
        window.dispatchEvent(new CustomEvent('cart:changed', { detail: cart }));
    }
}

export const cart = {
    getCart(): Cart {
        return loadCart();
    },

    addToCart(productId: string, qtyDelta: number = 1) {
        const cart = loadCart();
        const existingItem = cart.items.find(item => item.id === productId);

        if (existingItem) {
            existingItem.qty += qtyDelta;
            if (existingItem.qty <= 0) {
                cart.items = cart.items.filter(item => item.id !== productId);
                saveCart(cart);
                return;
            }
        } else {
            if (qtyDelta > 0) {
                cart.items.push({ id: productId, qty: qtyDelta });
            }
        }

        saveCart(cart);
    },

    setQty(productId: string, qty: number) {
        const cart = loadCart();
        const item = cart.items.find(item => item.id === productId);

        if (item) {
            if (qty <= 0) {
                this.remove(productId);
                return;
            }
            item.qty = qty;
            saveCart(cart);
        }
    },

    remove(productId: string) {
        const cart = loadCart();
        cart.items = cart.items.filter(item => item.id !== productId);
        saveCart(cart);
    },

    clearCart() {
        const cart = { items: [] };
        saveCart(cart);
    },

    getCartCount(): number {
        const cart = loadCart();
        return cart.items.reduce((total, item) => total + item.qty, 0);
    },

    // Helper to calculate totals based on product data
    getCartDetailed(products: Product[]) {
        const cart = loadCart();
        const lineItems = cart.items.map(item => {
            const product = products.find(p => p.id === item.id);
            if (!product) return null;
            return {
                ...item,
                product,
                total: item.qty * product.price
            };
        }).filter(Boolean);

        const subtotal = lineItems.reduce((acc, item) => acc + (item?.total || 0), 0);

        return {
            lineItems,
            subtotal
        };
    }
};
