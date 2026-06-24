import sys

class Order:
    def __init__(self, id, customer_name, product_name, unit_price, quantity, shipping_fee, voucher):
        self.id = id
        self.customer_name = customer_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.shipping_fee = shipping_fee
        self.voucher = voucher
        self.total_amount = 0
        self.order_type = ""

        self.calculate_total_amount()
        self.classify_order()
    
    def calculate_total_amount(self):
        self.total_amount = (self.unit_price * self.quantity) + self.shipping_fee - self.voucher

    def classify_order(self):
        if self.total_amount >= 10000000:
            self.order_type = "VIP"
        elif self.total_amount >= 2000000:
            self.order_type = "Lớn"
        elif self.total_amount >= 500000:
            self.order_type = "Trung bình"
        else:
            self.order_type = "Nhỏ"

class OrderManager:
    def __init__(self):
        self.orders = []

    def show_all(self):
        print(f"{"Mã đơn hàng" :<20}"
                f"{"Tên khách hàng" :<15}"
                f"{"Tên sản phẩm" :<15}"
                f"{"Đơn giá" :<10}"
                f"{"Số lượng" :<5}"
                f"{"Phí vận chuyển" :<10}"
                f"{"Voucher" :<8}"
                f"{"Tổng tiền" :<10}"
                f"{"Phân loại đơn hàng" :<10}")   

        for order in self.orders:
            print(f"{order.id :<20}"
                f"{order.customer_name :<15}"
                f"{order.product_name :<15}"
                f"{order.unit_price :<10}"
                f"{order.quantity :<5}"
                f"{order.shipping_fee :<10}"
                f"{order.voucher :<8}"
                f"{order.total_amount :<10}"
                f"{order.order_type :<10}")   


    def add_order(self):
        print("\n =========== Thêm sản phẩm ===========")
        while True:
            order_id = input("Nhập vào mã đơn hàng: ")
            if not order_id:
                print("Không được để trống mã đơn hàng vui lòng nhập lại!!!")
                continue
            if order_id == self.id:
                print("Mã đơn hàng không được trùng lập!!!")
                continue
            break

        order_customer_name = input("Nhập vào tên khách hàng: ")
        order_product_name = input("Nhập vào tên sản phẩm: ")
        order_unit_price = input("Nhập vào đơn giấ sản phẩm: ")
        order_quantity = input("Nhập vào số lượng: ")
        order_shipping_fee = input("Nhập vào giá vận chuyển: ")
        order_voucher = input("Nhập vào voucher của sản phẩm: ")

        new_order = Order(order_customer_name, order_product_name, order_unit_price, order_quantity, order_shipping_fee, order_voucher)
        self.orders = Order.append(new_order)

    def update_order(self):
        print("\n =========== Sửa sản phẩm ===========")
        while True:
            order_id = input("Nhập vào mã đơn hàng: ")
            if not order_id:
                print("Không được để trống mã đơn hàng vui lòng nhập lại!!!")
                continue
            if order_id == self.id:
                print("Tìm thấy sản phẩm cần cập nhật !!!")
                break
        
        self.customer_name = input("Nhập vào tên khách hàng cần sửa: ")
        self.product_name = input("Nhập vào tên sản phẩm cần sửa: ")
        self.unit_price = input("Nhập vào đơn giá sản phẩm cần sửa: ")
        self.quantity = input("Nhập vào số lượng cần sửa: ")
        self.shipping_fee = input("Nhập vào số tiền vận chuyển cần sửa: ")
        self.voucher = input("Nhập vào voucher cần sửa: ")

        self.calculate_total_amount()
        self.classify_order()

        print(f"Đã cập nhật thành công mã sản phẩm {order_id}!!!")
        

    def delete_order(self):
        print("\n =========== Sửa sản phẩm ===========")
        while True:
            order_id = input("Nhập vào mã đơn hàng: ")
            if not order_id:
                print("Không được để trống mã đơn hàng vui lòng nhập lại!!!")
                continue
            if order_id == self.id:
                print("Tìm thấy sản phẩm cần xóa !!!")
                break
        
        self.customer_name = input("Nhập vào tên khách hàng cần xóa: ")
        self.product_name = input("Nhập vào tên sản phẩm cần xóa: ")
        self.unit_price = input("Nhập vào đơn giá sản phẩm cần xóa: ")
        self.quantity = input("Nhập vào số lượng cần xóa: ")
        self.shipping_fee = input("Nhập vào số tiền vận chuyển cần xóa: ")
        self.voucher = input("Nhập vào voucher cần xóa: ")

        self.calculate_total_amount()
        self.classify_order()

        print(f"Đã xóa thành công mã sản phẩm {order_id}!!!")

    def search_order(self):
        pass

def menu():
    print("""\n
        ==================== MENU ====================
            1. Hiển thị danh sách đơn hàng
            2. Thêm đơn hàng mới 
            3. Cập nhật đơn hàng
            4. Xóa đơn hàng
            5. Tìm kiếm đơn hàng
            6. Thoát
        ===============================================
        """)
    
def main():
    order_manager = OrderManager()
    order_manager : {"DH001", "Nguyễn Văn Minh Tín", "Laptop", 500000, 1, 2000, 500}
    while True:
        menu()

        choice = input("Nhập lựa chọn của bạn (1 - 6): ")   

        match choice:
            case "1":
                OrderManager.show_all(order_manager)
            case "2":
                OrderManager.add_order(order_manager)
            case "3":
                OrderManager.update_order(order_manager)
            case "4":
                OrderManager.delete_order(order_manager)
            case "5":
                pass
            case "6":
                print("\n Thoát chương trình!!!")
                break
            case _:
                print("\n Lựa chọn không hợp lệ!!!")

if __name__ == "__main__":
    main()