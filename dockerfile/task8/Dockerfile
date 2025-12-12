FROM golang:1.19 AS builder
WORKDIR /app
COPY main.go .
ENV CGO_ENABLED=0
RUN go build -o hello main.go

FROM scratch
COPY --from=builder /app/hello /hello

ENTRYPOINT ["/hello"]
EXPOSE 8999
