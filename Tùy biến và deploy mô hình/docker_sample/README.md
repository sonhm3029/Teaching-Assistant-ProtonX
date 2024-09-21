# Sử dụng cơ bản docker compose và volume

## Volume

Về cơ bản là sử dụng để ánh xạ folder từ máy chủ vào folder trong docker container

Câu lệnh:

```shell
docker run ... -v <host-folder>:<docker-folder>
```

Xem chi tiết:

[https://docs.docker.com/engine/storage/volumes/](https://docs.docker.com/engine/storage/volumes/)


## Network

Đối với các service chạy trên môi trường local (Chưa đóng gói thành container - môi trường phát triển) có thể dễ dàng tương tác qua lại thông qua địa chỉ `localhost`. Tuy nhiên khi đóng gói thành container, tuy rằng các container này có thể nằm trên cùng một máy chủ nhưng các container hoạt động độc lập trên mạng riêng vì thế không thể tương tác thông qua địa chỉ `localhost` nữa, mà cần chỉ có thể giao tiếp bằng địa chỉ IP máy chủ mà các container đang chạy trên đó.

Đọc thêm:

- [https://docker-curriculum.com/#docker-network](https://docker-curriculum.com/#docker-network)

## Docker compose

Một tool của docker để quản lý nhiều container cùng một lúc mà chỉ cần dùng 1 file yaml duy nhất.

Các lệnh cơ bản (Lưu ý sử dụng tại folder chứa docker-compose.yaml file):

```shell
# Chạy tất cả các service với chế độ ngầm --detach
docker-compose up -d

# Xem các container được quản lý bởi docker-compose
docker-compose ps

# Dừng các container đã được chạy bằng docker-compose
docker-compose down
```

Xem chi tiết tại:

- [https://docs.docker.com/compose/](https://docs.docker.com/compose/)