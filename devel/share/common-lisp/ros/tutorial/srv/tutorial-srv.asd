
(cl:in-package :asdf)

(defsystem "tutorial-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "services" :depends-on ("_package_services"))
    (:file "_package_services" :depends-on ("_package"))
  ))